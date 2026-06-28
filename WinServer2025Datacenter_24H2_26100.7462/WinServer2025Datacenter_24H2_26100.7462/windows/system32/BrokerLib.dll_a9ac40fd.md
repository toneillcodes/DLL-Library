# Binary Specification: BrokerLib.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BrokerLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a9ac40fda7e9c730e486a35adfa5e68a69881007f67bdc635731c94cb6554741`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 28 | `BrQueryBrokeredEvents2` | `0x2CF0` | 469 | UnwindData |  |
| 26 | `BrQueryBrokeredApplicationState` | `0x68C0` | 781 | UnwindData |  |
| 34 | `BrSignalBrokerEvent2` | `0x9360` | 39 | UnwindData |  |
| 36 | `BrUnlockBroker` | `0xA5C0` | 235 | UnwindData |  |
| 25 | `BrLockBroker` | `0xA6C0` | 235 | UnwindData |  |
| 18 | `BrGetBrokeredEventInfo2` | `0xA7C0` | 537 | UnwindData |  |
| 35 | `BrSignalBrokerEvent2Ex` | `0xA9E0` | 428 | UnwindData |  |
| 16 | `BrGetBrokeredAppState2` | `0xB7F0` | 731 | UnwindData |  |
| 27 | `BrQueryBrokeredEvents` | `0xD6F0` | 466 | UnwindData |  |
| 13 | `BrFindBrokeredEvent` | `0xD8D0` | 470 | UnwindData |  |
| 14 | `BrFindBrokeredEvent2` | `0xDC00` | 483 | UnwindData |  |
| 19 | `BrGetBrokeredEventState` | `0x141B0` | 204 | UnwindData |  |
| 20 | `BrGetPackageFullNameForBrokeredEvent` | `0x14850` | 406 | UnwindData |  |
| 24 | `BrInitializeBrokerInstance2` | `0x14B50` | 179 | UnwindData |  |
| 2 | `BrBufferFree` | `0x152A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BrCheckCallerCapabilities2` | `0x152E0` | 308 | UnwindData |  |
| 7 | `BrCreateBrokerInstance2` | `0x15900` | 163 | UnwindData |  |
| 10 | `BrDeleteBrokerInstance` | `0x16060` | 201 | UnwindData |  |
| 1 | `BrCreateBrokeredEvent2` | `0x19BF0` | 273 | UnwindData |  |
| 3 | `BrCheckCallerCapabilities` | `0x19D80` | 223 | UnwindData |  |
| 5 | `BrCheckCallerIsAppContainer` | `0x19E70` | 109 | UnwindData |  |
| 6 | `BrCreateBrokerInstance` | `0x19EF0` | 147 | UnwindData |  |
| 8 | `BrCreateBrokeredEvent` | `0x19F90` | 236 | UnwindData |  |
| 9 | `BrDecQuota` | `0x1A090` | 387 | UnwindData |  |
| 11 | `BrDeleteBrokeredEvent` | `0x1A220` | 154 | UnwindData |  |
| 12 | `BrDeleteBrokeredEvent2` | `0x1A2C0` | 222 | UnwindData |  |
| 15 | `BrGetBrokeredAppState` | `0x1A3B0` | 237 | UnwindData |  |
| 17 | `BrGetBrokeredAppStateName` | `0x1A4B0` | 209 | UnwindData |  |
| 21 | `BrGetQuota` | `0x1A590` | 397 | UnwindData |  |
| 22 | `BrIncQuota` | `0x1A730` | 387 | UnwindData |  |
| 23 | `BrInitializeBrokerInstance` | `0x1A8C0` | 138 | UnwindData |  |
| 29 | `BrRegisterBrokeredEvent` | `0x1A950` | 218 | UnwindData |  |
| 30 | `BrRegisterStateChangeCallbacks` | `0x1AA30` | 158 | UnwindData |  |
| 31 | `BrSendActivatorControl` | `0x1AAE0` | 209 | UnwindData |  |
| 32 | `BrSetBrokeredAppStateName` | `0x1ABC0` | 205 | UnwindData |  |
| 33 | `BrSignalBrokerEvent` | `0x1ACA0` | 321 | UnwindData |  |
| 37 | `BrUnregisterBrokeredEvent` | `0x1ADF0` | 158 | UnwindData |  |
