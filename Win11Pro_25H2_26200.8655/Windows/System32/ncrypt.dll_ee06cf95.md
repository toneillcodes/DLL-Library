# Binary Specification: ncrypt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ncrypt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee06cf953c62806ca9fdc91361e21f1c61506ed846e0a67a749de50464207f70`
* **Total Exported Functions:** 162

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
| 127 | `SslEnumEccCurves` | `0x1090` | 408 | UnwindData |  |
| 106 | `NCryptTranslateHandle` | `0x1230` | 2,047 | UnwindData |  |
| 76 | `NCryptEnumAlgorithms` | `0x1AD0` | 588 | UnwindData |  |
| 126 | `SslEnumCipherSuitesEx` | `0x2000` | 683 | UnwindData |  |
| 158 | `SslOpenProvider` | `0x2320` | 816 | UnwindData |  |
| 77 | `NCryptEnumKeys` | `0x2660` | 883 | UnwindData |  |
| 91 | `NCryptOpenKeyProtector` | `0x2F60` | 772 | UnwindData |  |
| 85 | `NCryptImportKey` | `0x37C0` | 2,019 | UnwindData |  |
| 144 | `SslGenerateMasterKey` | `0x4470` | 588 | UnwindData |  |
| 146 | `SslGenerateSessionKeys` | `0x46D0` | 592 | UnwindData |  |
| 147 | `SslGetCipherSuitePRFHashAlgorithm` | `0x4930` | 337 | UnwindData |  |
| 154 | `SslIncrementProviderReferenceCount` | `0x4A90` | 68 | UnwindData |  |
| 117 | `SslCreateClientAuthHash` | `0x5580` | 626 | UnwindData |  |
| 97 | `NCryptSecretAgreement` | `0x5CE0` | 63 | UnwindData |  |
| 100 | `NCryptSignHash` | `0x6070` | 68 | UnwindData |  |
| 92 | `NCryptOpenStorageProvider` | `0x6660` | 999 | UnwindData |  |
| 155 | `SslLookupCipherLengths` | `0x6A50` | 338 | UnwindData |  |
| 143 | `SslFreeObject` | `0x6BB0` | 1,310 | UnwindData |  |
| 124 | `SslEncryptPacket` | `0x70E0` | 1,062 | UnwindData |  |
| 151 | `SslHashHandshake` | `0x7510` | 930 | UnwindData |  |
| 82 | `NCryptFreeObject` | `0x7900` | 500 | UnwindData |  |
| 137 | `SslExportKey` | `0x7F00` | 1,050 | UnwindData |  |
| 121 | `SslDecryptPacket` | `0x8320` | 1,102 | UnwindData |  |
| 67 | `NCryptCreatePersistedKey` | `0x8850` | 81 | UnwindData |  |
| 83 | `NCryptGetProperty` | `0x8C00` | 142 | UnwindData |  |
| 133 | `SslExpandPreSharedKey` | `0x9360` | 589 | UnwindData |  |
| 90 | `NCryptOpenKey` | `0x95C0` | 62 | UnwindData |  |
| 120 | `SslDecrementProviderReferenceCount` | `0x98F0` | 188 | UnwindData |  |
| 116 | `SslComputeSessionHash` | `0x9AE0` | 337 | UnwindData |  |
| 156 | `SslLookupCipherSuiteInfo` | `0x9C40` | 221 | UnwindData |  |
| 72 | `NCryptDeriveKey` | `0x9D30` | 328 | UnwindData |  |
| 135 | `SslExpandTrafficKeys` | `0xA0D0` | 829 | UnwindData |  |
| 64 | `NCryptCloseKeyProtector` | `0xA420` | 290 | UnwindData |  |
| 81 | `NCryptFreeBuffer` | `0xAB80` | 159 | UnwindData |  |
| 108 | `NCryptUnprotectSecret` | `0xAFE0` | 959 | UnwindData |  |
| 65 | `NCryptCloseProtectionDescriptor` | `0xB3B0` | 151 | UnwindData |  |
| 94 | `NCryptProtectSecret` | `0xCB20` | 1,726 | UnwindData |  |
| 102 | `NCryptStreamOpenToProtect` | `0xEF90` | 966 | UnwindData |  |
| 105 | `NCryptStreamUpdate` | `0xF380` | 1,174 | UnwindData |  |
| 103 | `NCryptStreamOpenToUnprotect` | `0x10060` | 340 | UnwindData |  |
| 136 | `SslExpandWriteKey` | `0x10420` | 577 | UnwindData |  |
| 71 | `NCryptDeleteKey` | `0x10670` | 424 | UnwindData |  |
| 75 | `NCryptEncrypt` | `0x10820` | 501 | UnwindData |  |
| 79 | `NCryptExportKey` | `0x10A20` | 74 | UnwindData |  |
| 110 | `NCryptVerifySignature` | `0x10D70` | 560 | UnwindData |  |
| 87 | `NCryptIsKeyHandle` | `0x10FB0` | 25 | UnwindData |  |
| 70 | `NCryptDecrypt` | `0x10FD0` | 618 | UnwindData |  |
| 88 | `NCryptKeyDerivation` | `0x11240` | 648 | UnwindData |  |
| 80 | `NCryptFinalizeKey` | `0x114F0` | 322 | UnwindData |  |
| 113 | `SslComputeClientAuthHash` | `0x116F0` | 263 | UnwindData |  |
| 140 | `SslExtractHandshakeKey` | `0x11830` | 519 | UnwindData |  |
| 115 | `SslComputeFinishedHash` | `0x11A40` | 338 | UnwindData |  |
| 139 | `SslExtractEarlyKey` | `0x11BA0` | 85 | UnwindData |  |
| 131 | `SslExpandExporterMasterKey` | `0x11E40` | 578 | UnwindData |  |
| 134 | `SslExpandResumptionMasterKey` | `0x12090` | 675 | UnwindData |  |
| 119 | `SslCreateHandshakeHash` | `0x12340` | 494 | UnwindData |  |
| 152 | `SslImportKey` | `0x12540` | 505 | UnwindData |  |
| 148 | `SslGetKeyProperty` | `0x12740` | 410 | UnwindData |  |
| 118 | `SslCreateEphemeralKey` | `0x128E0` | 610 | UnwindData |  |
| 141 | `SslExtractMasterKey` | `0x12B50` | 594 | UnwindData |  |
| 142 | `SslFreeBuffer` | `0x12DB0` | 79 | UnwindData |  |
| 130 | `SslExpandBinderKey` | `0x12EC0` | 594 | UnwindData |  |
| 160 | `SslSignHash` | `0x13120` | 303 | UnwindData |  |
| 66 | `NCryptCreateClaim` | `0x13610` | 571 | UnwindData |  |
| 129 | `SslEnumProtocolProviders` | `0x13CE0` | 685 | UnwindData |  |
| 93 | `NCryptProtectKey` | `0x14130` | 407 | UnwindData |  |
| 107 | `NCryptUnprotectKey` | `0x142D0` | 354 | UnwindData |  |
| 68 | `NCryptCreateProtectionDescriptor` | `0x14B40` | 756 | UnwindData |  |
| 78 | `NCryptEnumStorageProviders` | `0x150B0` | 636 | UnwindData |  |
| 153 | `SslImportMasterKey` | `0x15690` | 470 | UnwindData |  |
| 101 | `NCryptStreamClose` | `0x15E90` | 112 | UnwindData |  |
| 86 | `NCryptIsAlgSupported` | `0x16120` | 367 | UnwindData |  |
| 157 | `SslOpenPrivateKey` | `0x16300` | 300 | UnwindData |  |
| 99 | `NCryptSetProperty` | `0x177F0` | 2,457 | UnwindData |  |
| 125 | `SslEnumCipherSuites` | `0x18C10` | 534 | UnwindData |  |
| 111 | `SslChangeNotify` | `0x19820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `SslCombineKeys` | `0x19830` | 403 | UnwindData |  |
| 114 | `SslComputeEapKeyBlock` | `0x199D0` | 175 | UnwindData |  |
| 122 | `SslDeriveSessionTicketKey` | `0x19A90` | 353 | UnwindData |  |
| 123 | `SslDuplicateTranscriptHash` | `0x19C00` | 358 | UnwindData |  |
| 128 | `SslEnumGroups` | `0x19D70` | 280 | UnwindData |  |
| 132 | `SslExpandNextGenTrafficKey` | `0x19E90` | 364 | UnwindData |  |
| 138 | `SslExportKeyingMaterial` | `0x1A010` | 231 | UnwindData |  |
| 145 | `SslGeneratePreMasterKey` | `0x1A100` | 397 | UnwindData |  |
| 149 | `SslGetProviderProperty` | `0x1A2A0` | 474 | UnwindData |  |
| 150 | `SslGetSessionTicketProtectionHeaderSize` | `0x1A480` | 104 | UnwindData |  |
| 159 | `SslProtectSessionTicket` | `0x1A4F0` | 174 | UnwindData |  |
| 161 | `SslUnprotectSessionTicket` | `0x1A5B0` | 174 | UnwindData |  |
| 162 | `SslVerifySignature` | `0x1A670` | 159 | UnwindData |  |
| 61 | `GetIsolationServerInterface` | `0x1A9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `GetKeyStorageInterface` | `0x1A9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetSChannelInterface` | `0x1A9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `NCryptSetAuditingInterface` | `0x1AA00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `NCryptDecapsulate` | `0x1ACF0` | 484 | UnwindData |  |
| 74 | `NCryptEncapsulate` | `0x1AEE0` | 518 | UnwindData |  |
| 89 | `NCryptNotifyChangeKey` | `0x1B0F0` | 226 | UnwindData |  |
| 109 | `NCryptVerifyClaim` | `0x1B1E0` | 772 | UnwindData |  |
| 73 | `NCryptDuplicateKeyProtectorHandle` | `0x1BFB0` | 173 | UnwindData |  |
| 84 | `NCryptGetProtectionDescriptorInfo` | `0x1C070` | 160 | UnwindData |  |
| 95 | `NCryptQueryProtectionDescriptorName` | `0x1C120` | 366 | UnwindData |  |
| 96 | `NCryptRegisterProtectionDescriptorName` | `0x1C2A0` | 416 | UnwindData |  |
| 104 | `NCryptStreamOpenToUnprotectEx` | `0x1C450` | 233 | UnwindData |  |
