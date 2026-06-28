# Binary Specification: vrfcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vrfcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c8f53f6da63039c299cf9c2c71f7762ce33ae455e4744b652773aa1c7016f0dd`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AVrfAPILookupCallback` | `0x17F0` | 60 | UnwindData |  |
| 2 | `VerifierGetInfoForException` | `0x26B0` | 143 | UnwindData |  |
| 3 | `VerifierAreStaticDllsInitialized` | `0x2D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `VerifierChainDuplicateHooks` | `0x2DA0` | 476 | UnwindData |  |
| 5 | `VerifierCloseLayerProperties` | `0x2F90` | 27 | UnwindData |  |
| 6 | `VerifierConfigureStopOptions` | `0x2FC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `VerifierCreateLayerProperties` | `0x3010` | 192 | UnwindData |  |
| 16 | `VerifierGetLoggingDirectory` | `0x30E0` | 33 | UnwindData |  |
| 17 | `VerifierGetRecursionTlsSlot` | `0x3110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `VerifierHandleVerifierStopException` | `0x3120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `VerifierIsDllEntryActive` | `0x3130` | 56 | UnwindData |  |
| 20 | `VerifierIsInsideVerifierStop` | `0x3170` | 28 | UnwindData |  |
| 21 | `VerifierIsLayerEnabled` | `0x31A0` | 110 | UnwindData |  |
| 22 | `VerifierLdrGetProcedureAddress` | `0x3220` | 29 | UnwindData |  |
| 23 | `VerifierOpenLayerProperties` | `0x3250` | 185 | UnwindData |  |
| 24 | `VerifierQueryGlobalProperties` | `0x3310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VerifierQueryLayerBreak` | `0x3330` | 322 | UnwindData |  |
| 26 | `VerifierQueryLayerBreaks` | `0x3480` | 79 | UnwindData |  |
| 27 | `VerifierQueryLayerProperties` | `0x34E0` | 76 | UnwindData |  |
| 28 | `VerifierQueryLayerProperty` | `0x3540` | 136 | UnwindData |  |
| 38 | `VerifierSetLayerBreak` | `0x35D0` | 451 | UnwindData |  |
| 39 | `VerifierSetLayerProperty` | `0x37A0` | 165 | UnwindData |  |
| 41 | `VerifierStopMessageEx` | `0x3850` | 2,390 | UnwindData |  |
| 10 | `VerifierDisableLayer` | `0x8280` | 1,732 | UnwindData |  |
| 11 | `VerifierDisableVerifier` | `0x8950` | 873 | UnwindData |  |
| 14 | `VerifierEnableLayer` | `0x8CC0` | 1,826 | UnwindData |  |
| 15 | `VerifierGetAppCallerAddress` | `0x93F0` | 187 | UnwindData |  |
| 29 | `VerifierQueryRegisteredLayers` | `0x94C0` | 166 | UnwindData |  |
| 31 | `VerifierRegisterLayer` | `0x9570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `VerifierRegisterLayerEx` | `0x9590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `VerifierUnregisterLayer` | `0x95A0` | 283 | UnwindData |  |
| 43 | `VerifierTlsGetValue` | `0xB1E0` | 54 | UnwindData |  |
| 44 | `VerifierTlsSetValue` | `0xB220` | 62 | UnwindData |  |
| 33 | `VerifierRegisterProvider` | `0xC800` | 266 | UnwindData |  |
| 8 | `VerifierDisableFaultInjectionExclusionRange` | `0xCBF0` | 263 | UnwindData |  |
| 9 | `VerifierDisableFaultInjectionTargetRange` | `0xCD00` | 263 | UnwindData |  |
| 12 | `VerifierEnableFaultInjectionExclusionRange` | `0xCE10` | 287 | UnwindData |  |
| 13 | `VerifierEnableFaultInjectionTargetRange` | `0xCF40` | 287 | UnwindData |  |
| 30 | `VerifierRegisterFaultInjectProvider` | `0xD070` | 151 | UnwindData |  |
| 34 | `VerifierResetFaultInjectionAddressRanges` | `0xD110` | 279 | UnwindData |  |
| 35 | `VerifierSetAPIClassName` | `0xD230` | 154 | UnwindData |  |
| 36 | `VerifierSetFaultInjectionProbability` | `0xD2D0` | 167 | UnwindData |  |
| 37 | `VerifierSetFaultInjectionSeed` | `0xD380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `VerifierShouldFaultInject` | `0xD3B0` | 326 | UnwindData |  |
| 42 | `VerifierSuspendFaultInjection` | `0xD500` | 125 | UnwindData |  |
