"""Cálculo determinista de contribución humana, sin dependencia del motor.

Los límites son por oficio según docs/04. No modifica reglas ni temporadas.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

PROFESSIONS = ("food", "wood", "mine", "build", "research")
FIRST_FULL = 100
LAST_COUNTED = 2500
FULL_BP = 10000
MARGINAL_BP = 2500
SCALE = 10000


@dataclass(frozen=True, slots=True)
class ActiveWorker:
    citizen_id: str
    profession: str
    active_since_utc: int


@dataclass(frozen=True, slots=True)
class WeightedWorker:
    citizen_id: str
    profession: str
    weight_bp: int


def assign_human_weights(workers: Iterable[ActiveWorker]) -> tuple[WeightedWorker, ...]:
    """Devuelve cuotas estables por oficio, ordenadas por antigüedad e ID.

    La entrada debe contener solo ciudadanos cuya actividad sigue vigente.
    La identidad es (profession, citizen_id) y duplicados se rechazan.
    """
    buckets: dict[str, list[ActiveWorker]] = {p: [] for p in PROFESSIONS}
    seen: set[tuple[str, str]] = set()
    for worker in workers:
        if worker.profession not in buckets:
            raise ValueError(f"Profesión desconocida: {worker.profession}")
        if not worker.citizen_id:
            raise ValueError("citizen_id vacío")
        key = (worker.profession, worker.citizen_id)
        if key in seen:
            raise ValueError(f"Ciudadano duplicado: {key}")
        seen.add(key)
        buckets[worker.profession].append(worker)

    result: list[WeightedWorker] = []
    for profession in PROFESSIONS:
        ordered = sorted(buckets[profession],
                         key=lambda x: (x.active_since_utc, x.citizen_id))
        for rank, worker in enumerate(ordered):
            weight = FULL_BP if rank < FIRST_FULL else (
                MARGINAL_BP if rank < LAST_COUNTED else 0
            )
            result.append(WeightedWorker(worker.citizen_id, profession, weight))
    return tuple(result)


def effective_worker_units_bp(weights: Iterable[WeightedWorker]) -> int:
    """Suma exacta en basis points; no redondea trabajadores equivalentes."""
    return sum(x.weight_bp for x in weights)


def output_milli_for_seconds(
    worker_seconds_bp: int,
    rate_milli_per_minute: int,
    multipliers_bp: tuple[int, ...] = (),
    remainder: int = 0,
) -> tuple[int, int]:
    """Calcula salida y resto exactos con un solo redondeo final.

    worker_seconds_bp suma (segundos trabajados * peso en basis points).
    remainder se expresa en unidades del denominador correspondiente;
    por tanto NO puede reutilizarse si cambia la lista de multiplicadores.
    """
    if worker_seconds_bp < 0 or rate_milli_per_minute < 0:
        raise ValueError("Producción negativa")
    if any(x < 0 for x in multipliers_bp):
        raise ValueError("Multiplicador negativo")
    denominator = 60 * SCALE ** (1 + len(multipliers_bp))
    if not 0 <= remainder < denominator:
        raise ValueError("Resto fuera de rango")
    numerator = worker_seconds_bp * rate_milli_per_minute
    for multiplier in multipliers_bp:
        numerator *= multiplier
    output, new_remainder = divmod(numerator + remainder, denominator)
    return output, new_remainder
