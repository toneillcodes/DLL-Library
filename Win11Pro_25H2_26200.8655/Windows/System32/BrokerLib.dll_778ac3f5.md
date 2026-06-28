# Binary Specification: BrokerLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BrokerLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `778ac3f558bcad91fd3bb683b1b94759ad696a8f0f1503027dd7445a6d196e46`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 28 | `BrQueryBrokeredEvents2` | `0x3130` | 469 | UnwindData |  |
| 26 | `BrQueryBrokeredApplicationState` | `0x6550` | 781 | UnwindData |  |
| 35 | `BrSignalBrokerEvent2` | `0x8FF0` | 39 | UnwindData |  |
| 37 | `BrUnlockBroker` | `0xA250` | 235 | UnwindData |  |
| 25 | `BrLockBroker` | `0xA350` | 235 | UnwindData |  |
| 18 | `BrGetBrokeredEventInfo2` | `0xA450` | 537 | UnwindData |  |
| 36 | `BrSignalBrokerEvent2Ex` | `0xA670` | 428 | UnwindData |  |
| 16 | `BrGetBrokeredAppState2` | `0xB480` | 731 | UnwindData |  |
| 27 | `BrQueryBrokeredEvents` | `0xE780` | 466 | UnwindData |  |
| 13 | `BrFindBrokeredEvent` | `0xE960` | 470 | UnwindData |  |
| 14 | `BrFindBrokeredEvent2` | `0xEC90` | 483 | UnwindData |  |
| 19 | `BrGetBrokeredEventState` | `0x14590` | 204 | UnwindData |  |
| 20 | `BrGetPackageFullNameForBrokeredEvent` | `0x14C50` | 406 | UnwindData |  |
| 24 | `BrInitializeBrokerInstance2` | `0x14ED0` | 179 | UnwindData |  |
| 2 | `BrBufferFree` | `0x15620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BrCheckCallerCapabilities2` | `0x15660` | 308 | UnwindData |  |
| 7 | `BrCreateBrokerInstance2` | `0x15C80` | 163 | UnwindData |  |
| 10 | `BrDeleteBrokerInstance` | `0x163E0` | 201 | UnwindData |  |
| 1 | `BrCreateBrokeredEvent2` | `0x1A000` | 273 | UnwindData |  |
| 3 | `BrCheckCallerCapabilities` | `0x1A190` | 223 | UnwindData |  |
| 5 | `BrCheckCallerIsAppContainer` | `0x1A280` | 109 | UnwindData |  |
| 6 | `BrCreateBrokerInstance` | `0x1A300` | 147 | UnwindData |  |
| 8 | `BrCreateBrokeredEvent` | `0x1A3A0` | 236 | UnwindData |  |
| 9 | `BrDecQuota` | `0x1A4A0` | 387 | UnwindData |  |
| 11 | `BrDeleteBrokeredEvent` | `0x1A630` | 154 | UnwindData |  |
| 12 | `BrDeleteBrokeredEvent2` | `0x1A6D0` | 222 | UnwindData |  |
| 15 | `BrGetBrokeredAppState` | `0x1A7C0` | 237 | UnwindData |  |
| 17 | `BrGetBrokeredAppStateName` | `0x1A8C0` | 209 | UnwindData |  |
| 21 | `BrGetQuota` | `0x1A9A0` | 397 | UnwindData |  |
| 22 | `BrIncQuota` | `0x1AB40` | 387 | UnwindData |  |
| 23 | `BrInitializeBrokerInstance` | `0x1ACD0` | 138 | UnwindData |  |
| 29 | `BrRegisterBrokeredEvent` | `0x1AD60` | 218 | UnwindData |  |
| 30 | `BrRegisterStateChangeCallbacks` | `0x1AE40` | 158 | UnwindData |  |
| 31 | `BrRemoveBrokeredEvent` | `0x1AEF0` | 289 | UnwindData |  |
| 32 | `BrSendActivatorControl` | `0x1B020` | 209 | UnwindData |  |
| 33 | `BrSetBrokeredAppStateName` | `0x1B100` | 205 | UnwindData |  |
| 34 | `BrSignalBrokerEvent` | `0x1B1E0` | 321 | UnwindData |  |
| 38 | `BrUnregisterBrokeredEvent` | `0x1B330` | 158 | UnwindData |  |
