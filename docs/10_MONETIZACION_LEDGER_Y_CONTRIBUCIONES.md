# 10 — Monetización verificable, ledger y límites

## Criterio de elegibilidad
`ContributionEvent` proviene de canal con `contributions` habilitado por operador; se requiere autenticación del origen, identificador estable, evidencia verificable del tipo/importe, estado económico final admisible y `conversionRuleVersion` activa para esa **plataforma, canal, tipo y moneda/unidad**. No se deduce equivalencia por texto libre, reacción, follower ni cantidad de likes. El proveedor puede cambiar campos, permisos, elegibilidad y reglas. Por defecto **todos los tipos reales de monetización están deshabilitados**, y no hay cambio automático a habilitado sin prueba con cuenta real. El juego gratuito funciona íntegramente así.

## Conversión y ejemplos
Conversión exacta por `provider, eventType, unit, ruleVersion`: `goldUnits=floor(verifiedAmountMinorUnits * numerator / denominator)`; guardar resto solo dentro del evento y sin inventar crédito. La configuración demo exclusivamente sintética define `provider=simulated, unit=DEMO, eventType=test_contribution, numerator=1, denominator=1`, a usar únicamente bajo `mode=SIMULATION`, jamás en entorno LIVE. Para plataformas reales se publica tabla tras revisar APIs y términos, no se escriben tasas falsas ni se atribuyen precios a regalos. Nunca se hacen conversiones genéricas entre monedas de proveedores.

## Estados de ingreso
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED` o `REJECTED`; también `REVERSED` tras `CREDITED` si existe evidencia de devolución/cancelación. Un evento reintentado produce un solo crédito gracias a unique `(provider, eventId, channelId, eventType)`. `CREDITED` añade al ledger oro y a tesorería de nación, no al bolsillo individual del donante. Cambio posterior de reglas no recalcula histórico.

## Reversos tras gasto
Si una reversión deja sin cobertura el hold de una votación abierta, la votación se cancela en la misma transacción y el hold se libera antes del asiento de reverso. Si se revierte el oro ya gastado, el saldo disponible se reduce hasta cero y el resto se registra como `goldDebtUnits` sin saldo negativo y sin tocar construcciones completadas; los siguientes ingresos verificables pagan deuda primero. El patronazgo queda marcado `reversed` y puede perder el reconocimiento visual conforme a política anunciada; no hay devolución automática por el videojuego ni política de compensación externa. La contabilidad interna del oro nunca reclama ser un balance de dinero fiduciario.

## Protección de jugador y monetización sana
Prohibido transferir oro, convertirlo en dinero real, apuestas, premios de valor real, bonificación de voto o condición de avanzar de era. Los proyectos con oro son puramente estéticos/prestigio; ganar no se compra. UI muestra claramente si la cuenta no tiene donaciones habilitadas. Mostrar estado de agradecimiento privado y nombres solo con moderación y criterios de privacidad. Cualquier funcionamiento de monetización requiere revisión legal, fiscal, de proveedor y tests de auditoría; estas condiciones no son definibles por documentos internos.
