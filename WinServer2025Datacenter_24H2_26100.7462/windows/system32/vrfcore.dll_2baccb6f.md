# Binary Specification: vrfcore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vrfcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2baccb6f014d5871b3f61adbef5259f21b716ab1f1c32417baa86a54b6637a5c`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AVrfAPILookupCallback` | `0x17F0` | 60 | UnwindData |  |
| 2 | `VerifierGetInfoForException` | `0x2670` | 140 | UnwindData |  |
| 3 | `VerifierAreStaticDllsInitialized` | `0x2CE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `VerifierChainDuplicateHooks` | `0x2D40` | 478 | UnwindData |  |
| 5 | `VerifierCloseLayerProperties` | `0x2F30` | 27 | UnwindData |  |
| 6 | `VerifierConfigureStopOptions` | `0x2F60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `VerifierCreateLayerProperties` | `0x2FB0` | 189 | UnwindData |  |
| 16 | `VerifierGetLoggingDirectory` | `0x3080` | 33 | UnwindData |  |
| 17 | `VerifierGetRecursionTlsSlot` | `0x30B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `VerifierHandleVerifierStopException` | `0x30C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `VerifierIsDllEntryActive` | `0x30D0` | 56 | UnwindData |  |
| 20 | `VerifierIsInsideVerifierStop` | `0x3110` | 28 | UnwindData |  |
| 21 | `VerifierIsLayerEnabled` | `0x3140` | 110 | UnwindData |  |
| 22 | `VerifierLdrGetProcedureAddress` | `0x31C0` | 29 | UnwindData |  |
| 23 | `VerifierOpenLayerProperties` | `0x31F0` | 182 | UnwindData |  |
| 24 | `VerifierQueryGlobalProperties` | `0x32B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VerifierQueryLayerBreak` | `0x32D0` | 322 | UnwindData |  |
| 26 | `VerifierQueryLayerBreaks` | `0x3420` | 79 | UnwindData |  |
| 27 | `VerifierQueryLayerProperties` | `0x3480` | 76 | UnwindData |  |
| 28 | `VerifierQueryLayerProperty` | `0x34E0` | 133 | UnwindData |  |
| 38 | `VerifierSetLayerBreak` | `0x3570` | 451 | UnwindData |  |
| 39 | `VerifierSetLayerProperty` | `0x3740` | 162 | UnwindData |  |
| 41 | `VerifierStopMessageEx` | `0x37F0` | 2,393 | UnwindData |  |
| 10 | `VerifierDisableLayer` | `0x8140` | 1,711 | UnwindData |  |
| 11 | `VerifierDisableVerifier` | `0x8800` | 873 | UnwindData |  |
| 14 | `VerifierEnableLayer` | `0x8B70` | 1,863 | UnwindData |  |
| 15 | `VerifierGetAppCallerAddress` | `0x92C0` | 184 | UnwindData |  |
| 29 | `VerifierQueryRegisteredLayers` | `0x9380` | 166 | UnwindData |  |
| 31 | `VerifierRegisterLayer` | `0x9430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `VerifierRegisterLayerEx` | `0x9450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `VerifierUnregisterLayer` | `0x9460` | 283 | UnwindData |  |
| 43 | `VerifierTlsGetValue` | `0xB080` | 54 | UnwindData |  |
| 44 | `VerifierTlsSetValue` | `0xB0C0` | 62 | UnwindData |  |
| 33 | `VerifierRegisterProvider` | `0xC680` | 266 | UnwindData |  |
| 8 | `VerifierDisableFaultInjectionExclusionRange` | `0xCA80` | 247 | UnwindData |  |
| 9 | `VerifierDisableFaultInjectionTargetRange` | `0xCB80` | 247 | UnwindData |  |
| 12 | `VerifierEnableFaultInjectionExclusionRange` | `0xCC80` | 287 | UnwindData |  |
| 13 | `VerifierEnableFaultInjectionTargetRange` | `0xCDB0` | 287 | UnwindData |  |
| 30 | `VerifierRegisterFaultInjectProvider` | `0xCEE0` | 151 | UnwindData |  |
| 34 | `VerifierResetFaultInjectionAddressRanges` | `0xCF80` | 255 | UnwindData |  |
| 35 | `VerifierSetAPIClassName` | `0xD090` | 154 | UnwindData |  |
| 36 | `VerifierSetFaultInjectionProbability` | `0xD130` | 167 | UnwindData |  |
| 37 | `VerifierSetFaultInjectionSeed` | `0xD1E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `VerifierShouldFaultInject` | `0xD210` | 320 | UnwindData |  |
| 42 | `VerifierSuspendFaultInjection` | `0xD360` | 125 | UnwindData |  |
