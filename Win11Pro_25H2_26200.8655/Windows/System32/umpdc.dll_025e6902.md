# Binary Specification: umpdc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\umpdc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `025e6902895a22b85279a672d39199b901600b56423050d1d3bd3aebd1f23c7f`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `Pdcv2ActivationClientDeactivate` | `0x1090` | 1,263 | UnwindData |  |
| 31 | `Pdcv2ActivationClientActivate` | `0x1960` | 2,630 | UnwindData |  |
| 34 | `Pdcv2ActivationClientRenewActivation` | `0x25B0` | 2,266 | UnwindData |  |
| 6 | `PdcFree` | `0x2F00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `Pdcv2ActivationClientSetBrokeredProcessId` | `0x31F0` | 340 | UnwindData |  |
| 43 | `SleepstudyHelperDestroyBlocker` | `0x35E0` | 23 | UnwindData |  |
| 48 | `SleepstudyHelperSetBlockerParentHandle` | `0x3740` | 133 | UnwindData |  |
| 39 | `SleepstudyHelperBuildBlocker` | `0x37D0` | 50 | UnwindData |  |
| 13 | `PdcPortSendMessageSynchronously` | `0x38D0` | 224 | UnwindData |  |
| 40 | `SleepstudyHelperCreateBlockerFromGuid` | `0x39C0` | 105 | UnwindData |  |
| 36 | `Pdcv2ActivationClientUnregister` | `0x3BD0` | 870 | UnwindData |  |
| 33 | `Pdcv2ActivationClientRegister` | `0x3F40` | 743 | UnwindData |  |
| 11 | `PdcPortOpen` | `0x48B0` | 978 | UnwindData |  |
| 22 | `PdcRwLockInitialize` | `0x4C90` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PdcPortClose` | `0x5260` | 6 | UnwindData |  |
| 29 | `PdcTaskClientRequest` | `0x56A0` | 54 | UnwindData |  |
| 24 | `PdcSignalClientRegister` | `0x57C0` | 65 | UnwindData |  |
| 3 | `PdcActivationClientRegister` | `0x5940` | 47 | UnwindData |  |
| 26 | `PdcSignalClientUnregister` | `0x5AA0` | 21 | UnwindData |  |
| 28 | `PdcTaskClientRegister` | `0x5B20` | 204 | UnwindData |  |
| 4 | `PdcActivationClientUnregister` | `0x5C00` | 30 | UnwindData |  |
| 14 | `PdcPpmProfileClientRegister` | `0x5DC0` | 223 | UnwindData |  |
| 30 | `PdcTaskClientUnregister` | `0x5EB0` | 29 | UnwindData |  |
| 2 | `PdcActivationClientActivityRequest` | `0x61A0` | 556 | UnwindData |  |
| 37 | `SleepstudyHelperBlockerActiveDereference` | `0x6CE0` | 23 | UnwindData |  |
| 38 | `SleepstudyHelperBlockerActiveReference` | `0x6E20` | 23 | UnwindData |  |
| 5 | `PdcAllocate` | `0x6F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PdcAcquireRwLockExclusive` | `0x6F90` | 43 | UnwindData |  |
| 7 | `PdcNotificationClientAcknowledge` | `0x6FD0` | 54 | UnwindData |  |
| 23 | `PdcSignalClientPulse` | `0x7100` | 166 | UnwindData |  |
| 12 | `PdcPortSendMessage` | `0x7700` | 195 | UnwindData |  |
| 18 | `PdcReleaseRwLockExclusive` | `0x7940` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `PdcPpmProfileEnable` | `0x79F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `PdcPpmProfileDisable` | `0x7A00` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `PdcSleep` | `0x7AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `PdcResiliencyClientRegister` | `0x7B00` | 84 | UnwindData |  |
| 42 | `SleepstudyHelperCreateLibraryEx` | `0x7C50` | 83 | UnwindData |  |
| 15 | `PdcPpmProfileClientUnregister` | `0x7D80` | 38 | UnwindData |  |
| 45 | `SleepstudyHelperDestroyLibrary` | `0x7E10` | 52 | UnwindData |  |
| 8 | `PdcNotificationClientRegister` | `0x8FF0` | 297 | UnwindData |  |
| 9 | `PdcNotificationClientUnregister` | `0x9120` | 191 | UnwindData |  |
| 19 | `PdcResiliencyClientAcknowledge` | `0x91F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `PdcResiliencyClientUnregister` | `0x9200` | 191 | UnwindData |  |
| 25 | `PdcSignalClientSetActive` | `0x93F0` | 109 | UnwindData |  |
| 41 | `SleepstudyHelperCreateLibrary` | `0x9470` | 36 | UnwindData |  |
| 44 | `SleepstudyHelperDestroyBlockerBuilder` | `0x94A0` | 125 | UnwindData |  |
| 46 | `SleepstudyHelperGetBlockerGuid` | `0x9530` | 137 | UnwindData |  |
| 47 | `SleepstudyHelperSetBlockerFriendlyName` | `0x95C0` | 186 | UnwindData |  |
| 49 | `SleepstudyHelperSetBlockerVisible` | `0x9680` | 124 | UnwindData |  |
