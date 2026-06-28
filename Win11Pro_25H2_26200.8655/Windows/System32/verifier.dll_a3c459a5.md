# Binary Specification: verifier.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\verifier.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a3c459a503022e3592a37067d5ac730b08083baef68e8c37d0db6976f2e3f1be`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `VerifierDisableFaultInjectionExclusionRange` | `0x1F20` | 192 | UnwindData |  |
| 8 | `VerifierDisableFaultInjectionTargetRange` | `0x1FF0` | 208 | UnwindData |  |
| 9 | `VerifierEnableFaultInjectionExclusionRange` | `0x20D0` | 179 | UnwindData |  |
| 10 | `VerifierEnableFaultInjectionTargetRange` | `0x2190` | 228 | UnwindData |  |
| 23 | `VerifierSetFaultInjectionProbability` | `0x2280` | 124 | UnwindData |  |
| 22 | `VerifierRedirectStopFunctions` | `0x7340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `VerifierStopMessage` | `0x7350` | 937 | UnwindData |  |
| 24 | `VerifierSetFlags` | `0x8DD0` | 402 | UnwindData |  |
| 1 | `AVrfAPILookupCallback` | `0x98D0` | 194 | UnwindData |  |
| 2 | `VerifierAddFreeMemoryCallback` | `0xA920` | 107 | UnwindData |  |
| 3 | `VerifierCheckPageHeapAllocation` | `0xA9A0` | 131 | UnwindData |  |
| 4 | `VerifierCreateRpcPageHeap` | `0xAA30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `VerifierDeleteFreeMemoryCallback` | `0xAA70` | 190 | UnwindData |  |
| 6 | `VerifierDestroyRpcPageHeap` | `0xAB40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `VerifierEnumerateResource` | `0xAB80` | 200 | UnwindData |  |
| 12 | `VerifierForceNormalHeap` | `0xAC50` | 98 | UnwindData |  |
| 13 | `VerifierGetInfoForException` | `0xACC0` | 140 | UnwindData |  |
| 14 | `VerifierGetMemoryForDump` | `0xAD60` | 149 | UnwindData |  |
| 15 | `VerifierGetPropertyValueByName` | `0xAE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `VerifierGetProviderHelper` | `0xAE10` | 141 | UnwindData |  |
| 17 | `VerifierIsAddressInAnyPageHeap` | `0xAEB0` | 379 | UnwindData |  |
| 18 | `VerifierIsCurrentThreadHoldingLocks` | `0xB040` | 55 | UnwindData |  |
| 19 | `VerifierIsDllEntryActive` | `0xB080` | 56 | UnwindData |  |
| 20 | `VerifierIsPerUserSettingsEnabled` | `0xB0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `VerifierQueryRuntimeFlags` | `0xB0E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VerifierSetRuntimeFlags` | `0xB140` | 107,644 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
