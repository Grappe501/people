# Module Dependency Matrix

**Governed by:** PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0  
**Legend:** `A` = ALLOW · `F` = FORBIDDEN · `P` = PORT/adapter only · `-` = N/A

## Layer × Layer

| From ↓ \\ To → | PRES | APP | DOM | INFRA | INT | WORK | SHARED |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRES | - | A | F | F | F | F | A |
| APP | F | - | A | P | P | F | A |
| DOM | F | F | - | F | F | F | A |
| INFRA | F | P | P | - | A | F | A |
| INT | F | P | F | A | - | F | A |
| WORK | F | A | F | F | F | - | A |
| SHARED | F | F | F | F | F | F | - |

## Capability collaboration (selected edges)

| Consumer | Provider | Mode | Notes |
| --- | --- | --- | --- |
| MOD-QUEUES | MOD-CLAIMS | Event / app port | Queue must not write claim rows |
| MOD-TRANSCRIPTIONS | MOD-DRAFTS | App port | Draft persistence owned by drafts |
| MOD-MATCHING | MOD-TRANSCRIPTIONS | Read port | Matching reads finalized transcription inputs via port |
| MOD-RESOLUTION | MOD-MATCHING | App/event | Resolution records decision; does not rescore privately |
| MOD-PROMOTION | MOD-RESOLUTION | App port | Promotion requires recorded resolution |
| MOD-PROMOTION | MOD-LAYER-INT | Port | Canonical person anti-corruption |
| MOD-CLAIMS | MOD-PAGES | Read port | Claim references page identity |
| MOD-UPLOADS | MOD-PAGES | App/event | Upload completion attaches page/image refs |
| MOD-NOTIFICATIONS | any detecting capability | Trigger in detector | Delivery via INT adapter |
| any mutator | MOD-AUDIT | Write port | No raw table writes |
| any privileged | MOD-PERMISSIONS / Catalog 5 | Check in APP | Keys from Catalog 5 |
| MOD-RETENTION | data-holding modules | Hook ports | No bypass deletes |
| MOD-LAYER-PRES | MOD-LAYER-APP | Direct | Only path for UI→business |
| MOD-LAYER-WORK | MOD-LAYER-APP | Direct | Workers never touch DOM/INFRA feature internals |

## Forbidden shortcuts (non-exhaustive)

| Forbidden edge | Reason |
| --- | --- |
| PRES → INFRA | UI bypass |
| PRES → INT | Provider leakage |
| WORK → INFRA repositories | Duplicate rules / missed audit |
| MATCHING → PROMOTION tables | Wrong owner |
| QUEUES → CLAIMS tables | Dual-write risk |
| SHARED → CLAIMS domain types | Hidden ownership |
| DOM → INT/INFRA | Provider coupling |

Any new ALLOW edge requires matrix amendment before coding.
