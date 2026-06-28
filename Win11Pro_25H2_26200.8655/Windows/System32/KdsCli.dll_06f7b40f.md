# Binary Specification: KdsCli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\KdsCli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `06f7b40fc9714623a4f169519423f4d40939426471d8a4bd3183f53571ef4730`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `GetDCInfo` | `0x2E90` | 1,563 | UnwindData |  |
| 22 | `GetDCInfoForLocalDC` | `0x34C0` | 1,208 | UnwindData |  |
| 26 | `GetKDSSrvConfigPath` | `0x3980` | 216 | UnwindData |  |
| 28 | `GetLdapBinding` | `0x3A60` | 629 | UnwindData |  |
| 29 | `GetMRKPath` | `0x3CE0` | 216 | UnwindData |  |
| 1 | `CreateRootKey` | `0x4B30` | 884 | UnwindData |  |
| 5 | `FreeRootKey` | `0x4EB0` | 169 | UnwindData |  |
| 6 | `FreeRootKeyConfig` | `0x4F60` | 86 | UnwindData |  |
| 7 | `FreeRootKeyMetaDataList` | `0x4FC0` | 86 | UnwindData |  |
| 14 | `GetAllRootKeys` | `0x53F0` | 448 | UnwindData |  |
| 15 | `GetAllRootKeysMetaData` | `0x55C0` | 635 | UnwindData |  |
| 30 | `GetRootKey` | `0x59D0` | 143 | UnwindData |  |
| 8 | `FreeServerConfig` | `0x6F90` | 36 | UnwindData |  |
| 23 | `GetDefaultServerConfig` | `0x71E0` | 164 | UnwindData |  |
| 33 | `GetServerConfig` | `0x7290` | 230 | UnwindData |  |
| 40 | `SetServerConfig` | `0x7CD0` | 301 | UnwindData |  |
| 43 | `ValidateKDFParam` | `0x7E10` | 180 | UnwindData |  |
| 44 | `ValidateSrvConfig` | `0x7ED0` | 251 | UnwindData |  |
| 2 | `DeleteAllCachedKeys` | `0x8380` | 504 | UnwindData |  |
| 3 | `FindAndReadSIDKeyInCache` | `0x8940` | 1,067 | UnwindData |  |
| 4 | `FindKeyForOfflineUsage` | `0x8D80` | 642 | UnwindData |  |
| 31 | `GetSIDKeyCacheFolder` | `0x93E0` | 469 | UnwindData |  |
| 32 | `GetSIDKeyFileName` | `0x95C0` | 490 | UnwindData |  |
| 45 | `WriteSIDKeyInCache` | `0xAA30` | 1,104 | UnwindData |  |
| 9 | `GenerateDerivedKey` | `0xB440` | 868 | UnwindData |  |
| 11 | `GenerateKDFContext` | `0xB7B0` | 205 | UnwindData |  |
| 10 | `GenerateEphemeralKeyPair` | `0xBAA0` | 527 | UnwindData |  |
| 12 | `GenerateSIDPublicKeyBlob` | `0xBCC0` | 303 | UnwindData |  |
| 13 | `GenerateSecretAgreementPrivateKey` | `0xBE00` | 1,457 | UnwindData |  |
| 41 | `TestServerConfig` | `0xC730` | 514 | UnwindData |  |
| 16 | `GetAndLockCachedRPCBinding` | `0xCB80` | 250 | UnwindData |  |
| 35 | `KdsCreateClientBinding` | `0xD570` | 981 | UnwindData |  |
| 42 | `UnlockRpcCache` | `0xDC80` | 61 | UnwindData |  |
| 17 | `GetCachedMachineDomainInfo` | `0xDEB0` | 487 | UnwindData |  |
| 18 | `GetCurrentIntervalID` | `0xE0A0` | 101 | UnwindData |  |
| 19 | `GetCurrentL0ID` | `0xE110` | 63 | UnwindData |  |
| 20 | `GetCurrentTimeInULL` | `0xE160` | 96 | UnwindData |  |
| 24 | `GetFullDCName` | `0xE1D0` | 318 | UnwindData |  |
| 25 | `GetIntervalStartTime` | `0xE320` | 116 | UnwindData |  |
| 27 | `GetKdsKeyCycleDuration` | `0xE3A0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetUserSidStr` | `0xE5E0` | 299 | UnwindData |  |
| 36 | `SIDKeyCopyBuffer` | `0xE8F0` | 131 | UnwindData |  |
| 37 | `SIDKeyCopyString` | `0xE980` | 210 | UnwindData |  |
| 38 | `SIDKeyProvAlloc` | `0xEA60` | 49 | UnwindData |  |
| 39 | `SIDKeyProvFree` | `0xEAA0` | 52 | UnwindData |  |
| 46 | `GetKey` | `0xEF00` | 109 | UnwindData |  |
| 47 | `KdsGetEpochLength` | `0x15A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `KdsGetGmsaPasswordBasedOnKeyId` | `0x15A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `KdsGetGmsaPasswordBasedOnTimestamp` | `0x15A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `KdsGetKeyStartTime` | `0x15A60` | 122 | UnwindData |  |
| 51 | `SIDKeyProtect` | `0x15FF0` | 1,470 | UnwindData |  |
| 52 | `SIDKeyUnprotect` | `0x165C0` | 1,098 | UnwindData |  |
