# Binary Specification: bcrypt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bcrypt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea17cd3093a3c7709a1de7532bd3af427101f5daaf100e74be654c07873b834c`
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
| 42 | `BCryptOpenAlgorithmProvider` | `0x9410` | 4,035 | UnwindData |  |
| 31 | `BCryptFreeBuffer` | `0xA3E0` | 98 | UnwindData |  |
| 41 | `BCryptKeyDerivation` | `0xA520` | 455 | UnwindData |  |
| 19 | `BCryptDuplicateKey` | `0xA6F0` | 641 | UnwindData |  |
| 53 | `BCryptSecretAgreement` | `0xA980` | 490 | UnwindData |  |
| 35 | `BCryptGetFipsAlgorithmMode` | `0xACC0` | 892 | UnwindData |  |
| 10 | `BCryptDecrypt` | `0xCF30` | 1,664 | UnwindData |  |
| 16 | `BCryptDestroyKey` | `0xD5C0` | 748 | UnwindData |  |
| 28 | `BCryptExportKey` | `0xD8C0` | 1,976 | UnwindData |  |
| 29 | `BCryptFinalizeKeyPair` | `0xE080` | 212 | UnwindData |  |
| 33 | `BCryptGenerateKeyPair` | `0xE160` | 261 | UnwindData |  |
| 39 | `BCryptImportKey` | `0xE3E0` | 889 | UnwindData |  |
| 40 | `BCryptImportKeyPair` | `0xE760` | 3,186 | UnwindData |  |
| 56 | `BCryptSetProperty` | `0xF3E0` | 596 | UnwindData |  |
| 57 | `BCryptSignHash` | `0xF640` | 1,225 | UnwindData |  |
| 60 | `BCryptVerifySignature` | `0xFB10` | 1,085 | UnwindData |  |
| 49 | `BCryptRegisterProvider` | `0x115E0` | 493 | UnwindData |  |
| 24 | `BCryptEnumContextFunctions` | `0x11CF0` | 567 | UnwindData |  |
| 55 | `BCryptSetContextFunctionProperty` | `0x12100` | 461 | UnwindData |  |
| 2 | `BCryptAddContextFunctionProvider` | `0x122E0` | 441 | UnwindData |  |
| 1 | `BCryptAddContextFunction` | `0x124A0` | 406 | UnwindData |  |
| 6 | `BCryptCreateContext` | `0x12640` | 377 | UnwindData |  |
| 8 | `BCryptCreateMultiHash` | `0x130B0` | 513 | UnwindData |  |
| 9 | `BCryptDecapsulate` | `0x132C0` | 295 | UnwindData |  |
| 20 | `BCryptEncapsulate` | `0x133F0` | 310 | UnwindData |  |
| 26 | `BCryptEnumProviders` | `0x13530` | 803 | UnwindData |  |
| 43 | `BCryptProcessMultiOperations` | `0x13860` | 123 | UnwindData |  |
| 54 | `BCryptSetAuditingInterface` | `0x138F0` | 16,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BCryptConfigureContext` | `0x17A10` | 367 | UnwindData |  |
| 5 | `BCryptConfigureContextFunction` | `0x17B90` | 406 | UnwindData |  |
| 11 | `BCryptDeleteContext` | `0x17D30` | 377 | UnwindData |  |
| 25 | `BCryptEnumContexts` | `0x17EB0` | 516 | UnwindData |  |
| 27 | `BCryptEnumRegisteredProviders` | `0x180C0` | 244 | UnwindData |  |
| 44 | `BCryptQueryContextConfiguration` | `0x181C0` | 471 | UnwindData |  |
| 45 | `BCryptQueryContextFunctionConfiguration` | `0x183A0` | 543 | UnwindData |  |
| 46 | `BCryptQueryContextFunctionProperty` | `0x185D0` | 570 | UnwindData |  |
| 48 | `BCryptRegisterConfigChangeNotify` | `0x18810` | 219 | UnwindData |  |
| 50 | `BCryptRemoveContextFunction` | `0x18900` | 394 | UnwindData |  |
| 51 | `BCryptRemoveContextFunctionProvider` | `0x18A90` | 426 | UnwindData |  |
| 58 | `BCryptUnregisterConfigChangeNotify` | `0x18C40` | 219 | UnwindData |  |
| 59 | `BCryptUnregisterProvider` | `0x18D30` | 275 | UnwindData |  |
