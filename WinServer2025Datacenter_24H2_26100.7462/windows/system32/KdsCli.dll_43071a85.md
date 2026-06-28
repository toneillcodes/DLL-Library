# Binary Specification: KdsCli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\KdsCli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `43071a85821bfa291d6e3b4dc7cf3253789861f1209400d5b0a6349802167e2c`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `GetDCInfo` | `0x1880` | 1,577 | UnwindData |  |
| 22 | `GetDCInfoForLocalDC` | `0x1EB0` | 1,208 | UnwindData |  |
| 26 | `GetKDSSrvConfigPath` | `0x2370` | 223 | UnwindData |  |
| 29 | `GetLdapBinding` | `0x2460` | 630 | UnwindData |  |
| 30 | `GetMRKPath` | `0x26E0` | 223 | UnwindData |  |
| 1 | `CreateRootKey` | `0x3550` | 884 | UnwindData |  |
| 5 | `FreeRootKey` | `0x38D0` | 165 | UnwindData |  |
| 6 | `FreeRootKeyConfig` | `0x3980` | 86 | UnwindData |  |
| 7 | `FreeRootKeyMetaDataList` | `0x39E0` | 86 | UnwindData |  |
| 14 | `GetAllRootKeys` | `0x3E10` | 448 | UnwindData |  |
| 15 | `GetAllRootKeysMetaData` | `0x3FE0` | 635 | UnwindData |  |
| 31 | `GetRootKey` | `0x43F0` | 143 | UnwindData |  |
| 8 | `FreeServerConfig` | `0x59D0` | 36 | UnwindData |  |
| 23 | `GetDefaultServerConfig` | `0x5C20` | 164 | UnwindData |  |
| 34 | `GetServerConfig` | `0x5CD0` | 230 | UnwindData |  |
| 45 | `SetServerConfig` | `0x6710` | 301 | UnwindData |  |
| 48 | `ValidateSrvConfig` | `0x6900` | 251 | UnwindData |  |
| 2 | `DeleteAllCachedKeys` | `0x6BA0` | 438 | UnwindData |  |
| 3 | `FindAndReadSIDKeyInCache` | `0x7020` | 1,067 | UnwindData |  |
| 4 | `FindKeyForOfflineUsage` | `0x7460` | 642 | UnwindData |  |
| 32 | `GetSIDKeyCacheFolder` | `0x7910` | 469 | UnwindData |  |
| 33 | `GetSIDKeyFileName` | `0x7AF0` | 497 | UnwindData |  |
| 49 | `WriteSIDKeyInCache` | `0x8610` | 1,104 | UnwindData |  |
| 9 | `GenerateDerivedKey` | `0x8AD0` | 875 | UnwindData |  |
| 11 | `GenerateKDFContext` | `0x8E50` | 205 | UnwindData |  |
| 10 | `GenerateEphemeralKeyPair` | `0x9140` | 527 | UnwindData |  |
| 12 | `GenerateSIDPublicKeyBlob` | `0x9360` | 303 | UnwindData |  |
| 13 | `GenerateSecretAgreementPrivateKey` | `0x94A0` | 1,464 | UnwindData |  |
| 46 | `TestServerConfig` | `0x9DD0` | 514 | UnwindData |  |
| 16 | `GetAndLockCachedRPCBinding` | `0xA220` | 250 | UnwindData |  |
| 36 | `KdsCreateClientBinding` | `0xAC20` | 981 | UnwindData |  |
| 47 | `UnlockRpcCache` | `0xB330` | 61 | UnwindData |  |
| 17 | `GetCachedMachineDomainInfo` | `0xB560` | 487 | UnwindData |  |
| 18 | `GetCurrentIntervalID` | `0xB750` | 101 | UnwindData |  |
| 19 | `GetCurrentL0ID` | `0xB7C0` | 63 | UnwindData |  |
| 20 | `GetCurrentTimeInULL` | `0xB810` | 96 | UnwindData |  |
| 24 | `GetFullDCName` | `0xB880` | 318 | UnwindData |  |
| 25 | `GetIntervalStartTime` | `0xB9D0` | 116 | UnwindData |  |
| 27 | `GetKdsKeyCycleDuration` | `0xBA50` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetUserSidStr` | `0xBC90` | 299 | UnwindData |  |
| 42 | `SIDKeyProvAlloc` | `0xBFA0` | 49 | UnwindData |  |
| 43 | `SIDKeyProvFree` | `0xBFE0` | 52 | UnwindData |  |
| 28 | `GetKey` | `0xC440` | 109 | UnwindData |  |
| 37 | `KdsGetEpochLength` | `0xC850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `KdsGetGmsaPasswordBasedOnKeyId` | `0xC870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `KdsGetGmsaPasswordBasedOnTimestamp` | `0xC880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `KdsGetKeyStartTime` | `0xC890` | 122 | UnwindData |  |
| 41 | `SIDKeyProtect` | `0xD610` | 1,476 | UnwindData |  |
| 44 | `SIDKeyUnprotect` | `0xDBE0` | 1,098 | UnwindData |  |
