# Binary Specification: bcrypt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\bcrypt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9ee5d54e9fbd795611322dd040e9978508c09091a6fdda40ea6f563e066da3ce`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `BCryptEnumAlgorithms` | `0x1690` | 1,011 | UnwindData |  |
| 13 | `BCryptDeriveKeyCapi` | `0x1E30` | 1,815 | UnwindData |  |
| 14 | `BCryptDeriveKeyPBKDF2` | `0x25D0` | 1,482 | UnwindData |  |
| 37 | `BCryptHash` | `0x2EE0` | 143 | UnwindData |  |
| 18 | `BCryptDuplicateHash` | `0x2F80` | 102 | UnwindData |  |
| 21 | `BCryptEncrypt` | `0x3300` | 1,267 | UnwindData |  |
| 3 | `BCryptCloseAlgorithmProvider` | `0x3E00` | 190 | UnwindData |  |
| 34 | `BCryptGenerateSymmetricKey` | `0x3ED0` | 819 | UnwindData |  |
| 7 | `BCryptCreateHash` | `0x4210` | 1,674 | UnwindData |  |
| 36 | `BCryptGetProperty` | `0x4AA0` | 1,108 | UnwindData |  |
| 15 | `BCryptDestroyHash` | `0x4F00` | 107 | UnwindData |  |
| 30 | `BCryptFinishHash` | `0x5090` | 144 | UnwindData |  |
| 38 | `BCryptHashData` | `0x5240` | 193 | UnwindData |  |
| 12 | `BCryptDeriveKey` | `0x54B0` | 190 | UnwindData |  |
| 23 | `BCryptEnumContextFunctionProviders` | `0x5EF0` | 522 | UnwindData |  |
| 52 | `BCryptResolveProviders` | `0x63B0` | 46 | UnwindData |  |
| 17 | `BCryptDestroySecret` | `0x7240` | 308 | UnwindData |  |
| 47 | `BCryptQueryProviderRegistration` | `0x83A0` | 483 | UnwindData |  |
| 32 | `BCryptGenRandom` | `0x8F00` | 519 | UnwindData |  |
| 42 | `BCryptOpenAlgorithmProvider` | `0x9410` | 4,067 | UnwindData |  |
| 31 | `BCryptFreeBuffer` | `0xA400` | 98 | UnwindData |  |
| 41 | `BCryptKeyDerivation` | `0xA540` | 455 | UnwindData |  |
| 19 | `BCryptDuplicateKey` | `0xA710` | 641 | UnwindData |  |
| 53 | `BCryptSecretAgreement` | `0xA9A0` | 490 | UnwindData |  |
| 35 | `BCryptGetFipsAlgorithmMode` | `0xACE0` | 892 | UnwindData |  |
| 10 | `BCryptDecrypt` | `0xCF50` | 1,664 | UnwindData |  |
| 16 | `BCryptDestroyKey` | `0xD5E0` | 748 | UnwindData |  |
| 28 | `BCryptExportKey` | `0xD8E0` | 1,976 | UnwindData |  |
| 29 | `BCryptFinalizeKeyPair` | `0xE0A0` | 212 | UnwindData |  |
| 33 | `BCryptGenerateKeyPair` | `0xE180` | 261 | UnwindData |  |
| 39 | `BCryptImportKey` | `0xE400` | 889 | UnwindData |  |
| 40 | `BCryptImportKeyPair` | `0xE780` | 3,186 | UnwindData |  |
| 56 | `BCryptSetProperty` | `0xF400` | 596 | UnwindData |  |
| 57 | `BCryptSignHash` | `0xF660` | 1,225 | UnwindData |  |
| 60 | `BCryptVerifySignature` | `0xFB30` | 1,085 | UnwindData |  |
| 49 | `BCryptRegisterProvider` | `0x11640` | 493 | UnwindData |  |
| 24 | `BCryptEnumContextFunctions` | `0x11D50` | 567 | UnwindData |  |
| 55 | `BCryptSetContextFunctionProperty` | `0x12160` | 461 | UnwindData |  |
| 2 | `BCryptAddContextFunctionProvider` | `0x12340` | 441 | UnwindData |  |
| 1 | `BCryptAddContextFunction` | `0x12500` | 406 | UnwindData |  |
| 6 | `BCryptCreateContext` | `0x126A0` | 377 | UnwindData |  |
| 8 | `BCryptCreateMultiHash` | `0x13110` | 513 | UnwindData |  |
| 9 | `BCryptDecapsulate` | `0x13320` | 295 | UnwindData |  |
| 20 | `BCryptEncapsulate` | `0x13450` | 310 | UnwindData |  |
| 26 | `BCryptEnumProviders` | `0x13590` | 803 | UnwindData |  |
| 43 | `BCryptProcessMultiOperations` | `0x138C0` | 123 | UnwindData |  |
| 54 | `BCryptSetAuditingInterface` | `0x13950` | 16,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BCryptConfigureContext` | `0x17A70` | 367 | UnwindData |  |
| 5 | `BCryptConfigureContextFunction` | `0x17BF0` | 406 | UnwindData |  |
| 11 | `BCryptDeleteContext` | `0x17D90` | 377 | UnwindData |  |
| 25 | `BCryptEnumContexts` | `0x17F10` | 516 | UnwindData |  |
| 27 | `BCryptEnumRegisteredProviders` | `0x18120` | 244 | UnwindData |  |
| 44 | `BCryptQueryContextConfiguration` | `0x18220` | 471 | UnwindData |  |
| 45 | `BCryptQueryContextFunctionConfiguration` | `0x18400` | 543 | UnwindData |  |
| 46 | `BCryptQueryContextFunctionProperty` | `0x18630` | 570 | UnwindData |  |
| 48 | `BCryptRegisterConfigChangeNotify` | `0x18870` | 219 | UnwindData |  |
| 50 | `BCryptRemoveContextFunction` | `0x18960` | 394 | UnwindData |  |
| 51 | `BCryptRemoveContextFunctionProvider` | `0x18AF0` | 426 | UnwindData |  |
| 58 | `BCryptUnregisterConfigChangeNotify` | `0x18CA0` | 219 | UnwindData |  |
| 59 | `BCryptUnregisterProvider` | `0x18D90` | 275 | UnwindData |  |
