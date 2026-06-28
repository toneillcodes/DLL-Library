# Binary Specification: ncrypt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ncrypt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f419b5f87ff0b521b18063c99d439234b6752540ea425f431ad5430f0da6912`
* **Total Exported Functions:** 160

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BCryptAddContextFunction` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptAddContextFunction` |
| 2 | `BCryptAddContextFunctionProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptAddContextFunctionProvider` |
| 3 | `BCryptCloseAlgorithmProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptCloseAlgorithmProvider` |
| 4 | `BCryptConfigureContext` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptConfigureContext` |
| 5 | `BCryptConfigureContextFunction` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptConfigureContextFunction` |
| 6 | `BCryptCreateContext` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptCreateContext` |
| 7 | `BCryptCreateHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptCreateHash` |
| 8 | `BCryptCreateMultiHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptCreateMultiHash` |
| 9 | `BCryptDecapsulate` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDecapsulate` |
| 10 | `BCryptDecrypt` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDecrypt` |
| 11 | `BCryptDeleteContext` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDeleteContext` |
| 12 | `BCryptDeriveKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDeriveKey` |
| 13 | `BCryptDeriveKeyCapi` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDeriveKeyCapi` |
| 14 | `BCryptDeriveKeyPBKDF2` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDeriveKeyPBKDF2` |
| 15 | `BCryptDestroyHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDestroyHash` |
| 16 | `BCryptDestroyKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDestroyKey` |
| 17 | `BCryptDestroySecret` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDestroySecret` |
| 18 | `BCryptDuplicateHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDuplicateHash` |
| 19 | `BCryptDuplicateKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptDuplicateKey` |
| 20 | `BCryptEncapsulate` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEncapsulate` |
| 21 | `BCryptEncrypt` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEncrypt` |
| 22 | `BCryptEnumAlgorithms` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumAlgorithms` |
| 23 | `BCryptEnumContextFunctionProviders` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumContextFunctionProviders` |
| 24 | `BCryptEnumContextFunctions` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumContextFunctions` |
| 25 | `BCryptEnumContexts` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumContexts` |
| 26 | `BCryptEnumProviders` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumProviders` |
| 27 | `BCryptEnumRegisteredProviders` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptEnumRegisteredProviders` |
| 28 | `BCryptExportKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptExportKey` |
| 29 | `BCryptFinalizeKeyPair` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptFinalizeKeyPair` |
| 30 | `BCryptFinishHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptFinishHash` |
| 31 | `BCryptFreeBuffer` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptFreeBuffer` |
| 32 | `BCryptGenRandom` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptGenRandom` |
| 33 | `BCryptGenerateKeyPair` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptGenerateKeyPair` |
| 34 | `BCryptGenerateSymmetricKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptGenerateSymmetricKey` |
| 35 | `BCryptGetFipsAlgorithmMode` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptGetFipsAlgorithmMode` |
| 36 | `BCryptGetProperty` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptGetProperty` |
| 37 | `BCryptHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptHash` |
| 38 | `BCryptHashData` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptHashData` |
| 39 | `BCryptImportKey` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptImportKey` |
| 40 | `BCryptImportKeyPair` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptImportKeyPair` |
| 41 | `BCryptKeyDerivation` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptKeyDerivation` |
| 42 | `BCryptOpenAlgorithmProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptOpenAlgorithmProvider` |
| 43 | `BCryptProcessMultiOperations` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptProcessMultiOperations` |
| 44 | `BCryptQueryContextConfiguration` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptQueryContextConfiguration` |
| 45 | `BCryptQueryContextFunctionConfiguration` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptQueryContextFunctionConfiguration` |
| 46 | `BCryptQueryContextFunctionProperty` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptQueryContextFunctionProperty` |
| 47 | `BCryptQueryProviderRegistration` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptQueryProviderRegistration` |
| 48 | `BCryptRegisterConfigChangeNotify` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptRegisterConfigChangeNotify` |
| 49 | `BCryptRegisterProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptRegisterProvider` |
| 50 | `BCryptRemoveContextFunction` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptRemoveContextFunction` |
| 51 | `BCryptRemoveContextFunctionProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptRemoveContextFunctionProvider` |
| 52 | `BCryptResolveProviders` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptResolveProviders` |
| 53 | `BCryptSecretAgreement` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptSecretAgreement` |
| 54 | `BCryptSetAuditingInterface` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptSetAuditingInterface` |
| 55 | `BCryptSetContextFunctionProperty` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptSetContextFunctionProperty` |
| 56 | `BCryptSetProperty` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptSetProperty` |
| 57 | `BCryptSignHash` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptSignHash` |
| 58 | `BCryptUnregisterConfigChangeNotify` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptUnregisterConfigChangeNotify` |
| 59 | `BCryptUnregisterProvider` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptUnregisterProvider` |
| 60 | `BCryptVerifySignature` | `0x0` | - | Forwarded | Forwarded to: `BCRYPT.BCryptVerifySignature` |
| 126 | `SslEnumEccCurves` | `0x1090` | 408 | UnwindData |  |
| 106 | `NCryptTranslateHandle` | `0x1230` | 2,047 | UnwindData |  |
| 76 | `NCryptEnumAlgorithms` | `0x1AD0` | 588 | UnwindData |  |
| 125 | `SslEnumCipherSuitesEx` | `0x2000` | 683 | UnwindData |  |
| 156 | `SslOpenProvider` | `0x2320` | 816 | UnwindData |  |
| 77 | `NCryptEnumKeys` | `0x2660` | 883 | UnwindData |  |
| 91 | `NCryptOpenKeyProtector` | `0x2F60` | 772 | UnwindData |  |
| 85 | `NCryptImportKey` | `0x37C0` | 2,019 | UnwindData |  |
| 142 | `SslGenerateMasterKey` | `0x4470` | 588 | UnwindData |  |
| 144 | `SslGenerateSessionKeys` | `0x46D0` | 592 | UnwindData |  |
| 145 | `SslGetCipherSuitePRFHashAlgorithm` | `0x4930` | 337 | UnwindData |  |
| 152 | `SslIncrementProviderReferenceCount` | `0x4A90` | 68 | UnwindData |  |
| 116 | `SslCreateClientAuthHash` | `0x5580` | 626 | UnwindData |  |
| 97 | `NCryptSecretAgreement` | `0x5D10` | 63 | UnwindData |  |
| 100 | `NCryptSignHash` | `0x60A0` | 68 | UnwindData |  |
| 92 | `NCryptOpenStorageProvider` | `0x6690` | 999 | UnwindData |  |
| 153 | `SslLookupCipherLengths` | `0x6A80` | 338 | UnwindData |  |
| 141 | `SslFreeObject` | `0x6BE0` | 1,310 | UnwindData |  |
| 123 | `SslEncryptPacket` | `0x7110` | 1,062 | UnwindData |  |
| 149 | `SslHashHandshake` | `0x7540` | 930 | UnwindData |  |
| 82 | `NCryptFreeObject` | `0x7930` | 500 | UnwindData |  |
| 135 | `SslExportKey` | `0x7FA0` | 1,050 | UnwindData |  |
| 120 | `SslDecryptPacket` | `0x83C0` | 1,102 | UnwindData |  |
| 67 | `NCryptCreatePersistedKey` | `0x88F0` | 81 | UnwindData |  |
| 83 | `NCryptGetProperty` | `0x8CA0` | 142 | UnwindData |  |
| 131 | `SslExpandPreSharedKey` | `0x9400` | 589 | UnwindData |  |
| 90 | `NCryptOpenKey` | `0x9660` | 62 | UnwindData |  |
| 119 | `SslDecrementProviderReferenceCount` | `0x9990` | 188 | UnwindData |  |
| 115 | `SslComputeSessionHash` | `0x9B80` | 337 | UnwindData |  |
| 154 | `SslLookupCipherSuiteInfo` | `0x9CE0` | 221 | UnwindData |  |
| 72 | `NCryptDeriveKey` | `0x9DD0` | 328 | UnwindData |  |
| 133 | `SslExpandTrafficKeys` | `0xA170` | 829 | UnwindData |  |
| 64 | `NCryptCloseKeyProtector` | `0xA4C0` | 290 | UnwindData |  |
| 81 | `NCryptFreeBuffer` | `0xAC20` | 159 | UnwindData |  |
| 108 | `NCryptUnprotectSecret` | `0xB080` | 959 | UnwindData |  |
| 65 | `NCryptCloseProtectionDescriptor` | `0xB450` | 151 | UnwindData |  |
| 94 | `NCryptProtectSecret` | `0xCBC0` | 1,726 | UnwindData |  |
| 102 | `NCryptStreamOpenToProtect` | `0xF030` | 966 | UnwindData |  |
| 105 | `NCryptStreamUpdate` | `0xF420` | 1,174 | UnwindData |  |
| 103 | `NCryptStreamOpenToUnprotect` | `0x10100` | 340 | UnwindData |  |
| 134 | `SslExpandWriteKey` | `0x104C0` | 577 | UnwindData |  |
| 71 | `NCryptDeleteKey` | `0x10710` | 424 | UnwindData |  |
| 75 | `NCryptEncrypt` | `0x108C0` | 501 | UnwindData |  |
| 79 | `NCryptExportKey` | `0x10AC0` | 74 | UnwindData |  |
| 110 | `NCryptVerifySignature` | `0x10E10` | 560 | UnwindData |  |
| 87 | `NCryptIsKeyHandle` | `0x11050` | 25 | UnwindData |  |
| 70 | `NCryptDecrypt` | `0x11070` | 618 | UnwindData |  |
| 88 | `NCryptKeyDerivation` | `0x112E0` | 648 | UnwindData |  |
| 80 | `NCryptFinalizeKey` | `0x11590` | 322 | UnwindData |  |
| 112 | `SslComputeClientAuthHash` | `0x11790` | 263 | UnwindData |  |
| 138 | `SslExtractHandshakeKey` | `0x118D0` | 519 | UnwindData |  |
| 114 | `SslComputeFinishedHash` | `0x11AE0` | 338 | UnwindData |  |
| 137 | `SslExtractEarlyKey` | `0x11C40` | 85 | UnwindData |  |
| 129 | `SslExpandExporterMasterKey` | `0x11EE0` | 578 | UnwindData |  |
| 132 | `SslExpandResumptionMasterKey` | `0x12130` | 675 | UnwindData |  |
| 118 | `SslCreateHandshakeHash` | `0x123E0` | 494 | UnwindData |  |
| 150 | `SslImportKey` | `0x125E0` | 505 | UnwindData |  |
| 146 | `SslGetKeyProperty` | `0x127E0` | 410 | UnwindData |  |
| 117 | `SslCreateEphemeralKey` | `0x12980` | 610 | UnwindData |  |
| 139 | `SslExtractMasterKey` | `0x12BF0` | 594 | UnwindData |  |
| 140 | `SslFreeBuffer` | `0x12E50` | 79 | UnwindData |  |
| 128 | `SslExpandBinderKey` | `0x12F60` | 594 | UnwindData |  |
| 158 | `SslSignHash` | `0x131C0` | 303 | UnwindData |  |
| 66 | `NCryptCreateClaim` | `0x136B0` | 571 | UnwindData |  |
| 127 | `SslEnumProtocolProviders` | `0x13F10` | 685 | UnwindData |  |
| 93 | `NCryptProtectKey` | `0x14360` | 407 | UnwindData |  |
| 107 | `NCryptUnprotectKey` | `0x14500` | 354 | UnwindData |  |
| 68 | `NCryptCreateProtectionDescriptor` | `0x14C30` | 756 | UnwindData |  |
| 78 | `NCryptEnumStorageProviders` | `0x151A0` | 636 | UnwindData |  |
| 151 | `SslImportMasterKey` | `0x15780` | 470 | UnwindData |  |
| 101 | `NCryptStreamClose` | `0x15F80` | 112 | UnwindData |  |
| 86 | `NCryptIsAlgSupported` | `0x16210` | 367 | UnwindData |  |
| 155 | `SslOpenPrivateKey` | `0x163F0` | 300 | UnwindData |  |
| 99 | `NCryptSetProperty` | `0x178E0` | 2,457 | UnwindData |  |
| 124 | `SslEnumCipherSuites` | `0x18D00` | 534 | UnwindData |  |
| 111 | `SslChangeNotify` | `0x19910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `SslComputeEapKeyBlock` | `0x19920` | 175 | UnwindData |  |
| 121 | `SslDeriveSessionTicketKey` | `0x199E0` | 353 | UnwindData |  |
| 122 | `SslDuplicateTranscriptHash` | `0x19B50` | 358 | UnwindData |  |
| 130 | `SslExpandNextGenTrafficKey` | `0x19CC0` | 364 | UnwindData |  |
| 136 | `SslExportKeyingMaterial` | `0x19E40` | 231 | UnwindData |  |
| 143 | `SslGeneratePreMasterKey` | `0x19F30` | 397 | UnwindData |  |
| 147 | `SslGetProviderProperty` | `0x1A0D0` | 474 | UnwindData |  |
| 148 | `SslGetSessionTicketProtectionHeaderSize` | `0x1A2B0` | 104 | UnwindData |  |
| 157 | `SslProtectSessionTicket` | `0x1A320` | 174 | UnwindData |  |
| 159 | `SslUnprotectSessionTicket` | `0x1A3E0` | 174 | UnwindData |  |
| 160 | `SslVerifySignature` | `0x1A4A0` | 159 | UnwindData |  |
| 61 | `GetIsolationServerInterface` | `0x1A820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `GetKeyStorageInterface` | `0x1A820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetSChannelInterface` | `0x1A820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `NCryptSetAuditingInterface` | `0x1A830` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `NCryptDecapsulate` | `0x1AB20` | 484 | UnwindData |  |
| 74 | `NCryptEncapsulate` | `0x1AD10` | 518 | UnwindData |  |
| 89 | `NCryptNotifyChangeKey` | `0x1AF20` | 226 | UnwindData |  |
| 109 | `NCryptVerifyClaim` | `0x1B010` | 772 | UnwindData |  |
| 73 | `NCryptDuplicateKeyProtectorHandle` | `0x1BD40` | 173 | UnwindData |  |
| 84 | `NCryptGetProtectionDescriptorInfo` | `0x1BE00` | 160 | UnwindData |  |
| 95 | `NCryptQueryProtectionDescriptorName` | `0x1BEB0` | 366 | UnwindData |  |
| 96 | `NCryptRegisterProtectionDescriptorName` | `0x1C030` | 416 | UnwindData |  |
| 104 | `NCryptStreamOpenToUnprotectEx` | `0x1C1E0` | 233 | UnwindData |  |
