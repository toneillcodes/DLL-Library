# Binary Specification: EventAggregation.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\EventAggregation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `01afd91d9b6a5ade7ec85e666ad0b495312096c3f80d6b07ef13750fdd5fa514`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `EaDeleteAggregatedEvent` | `0x1140` | 49 | UnwindData |  |
| 31 | `EaSignalAggregatedEvent` | `0x1400` | 39 | UnwindData |  |
| 17 | `EaCreateAggregation` | `0x1750` | 30 | UnwindData |  |
| 12 | `EACreateAggregateEvent` | `0x1D80` | 35 | UnwindData |  |
| 13 | `EADeleteAggregateEvent` | `0x2780` | 224 | UnwindData |  |
| 21 | `EaDeleteAggregation` | `0x2870` | 224 | UnwindData |  |
| 15 | `EAQueryAggregateEventData` | `0x2D00` | 28 | UnwindData |  |
| 5 | `BriDeleteBrokeredEvent` | `0x47A0` | 431 | UnwindData |  |
| 4 | `BriCreateBrokeredEventEx` | `0x4960` | 108 | UnwindData |  |
| 16 | `EaCreateAggregatedEvent` | `0x5880` | 192 | UnwindData |  |
| 8 | `BriIsBrokerRegistered` | `0x5B60` | 66 | UnwindData |  |
| 3 | `BriCreateBrokeredEvent` | `0x5C50` | 74 | UnwindData |  |
| 27 | `EaGetAggregation` | `0x6EF0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BriCleanup` | `0x7050` | 36 | UnwindData |  |
| 14 | `EAEnumerateAggregateEvents` | `0x7FF0` | 502 | UnwindData |  |
| 22 | `EaDisableAggregatedEvent` | `0x81F0` | 273 | UnwindData |  |
| 23 | `EaEnableAggregatedEvent` | `0x8310` | 268 | UnwindData |  |
| 28 | `EaQueryAggregateEventConditionState` | `0x8430` | 308 | UnwindData |  |
| 29 | `EaQueryAggregatedEvent` | `0x8570` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `BriAllocateRpcBuffer` | `0x8E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BriFreeRpcBuffer` | `0x8E70` | 20 | UnwindData |  |
| 7 | `BriGetBrokerAvailabilityChangeStamp` | `0x8E90` | 329 | UnwindData |  |
| 9 | `BriRegisterToBrokerAvailability` | `0x8FE0` | 344 | UnwindData |  |
| 10 | `BriResolveBrokerIdByEventId` | `0x9140` | 95 | UnwindData |  |
| 11 | `BriUnregisterFromBrokerAvailability` | `0x91B0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `EaFreeBuffer` | `0x9540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `EaDecodeBrokeredEvent` | `0x9550` | 182 | UnwindData |  |
| 20 | `EaDeleteAggregatedEventParameters` | `0x9610` | 139 | UnwindData |  |
| 24 | `EaEncodeBrokeredEvent` | `0x9820` | 190 | UnwindData |  |
| 25 | `EaFreeAggregatedEventParameters` | `0x98F0` | 100 | UnwindData |  |
| 30 | `EaQueryAggregatedEventParameters` | `0x9960` | 520 | UnwindData |  |
| 32 | `EaStoreAggregatedEventParameters` | `0x9B70` | 603 | UnwindData |  |
