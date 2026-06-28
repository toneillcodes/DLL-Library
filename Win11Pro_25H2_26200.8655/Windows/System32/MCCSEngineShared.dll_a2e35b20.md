# Binary Specification: MCCSEngineShared.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MCCSEngineShared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2e35b20d97a271172d282fe38f4c783b476ba6b7d316ca678fe4c27b7e30a02`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `DllCanUnloadNow` | `0x6290` | 42 | UnwindData |  |
| 34 | `DllGetClassObject` | `0x62C0` | 281 | UnwindData |  |
| 1 | `BuildISO8601String` | `0x6E60` | 291 | UnwindData |  |
| 2 | `BuildISO8601StringFromSysTime` | `0x6F90` | 313 | UnwindData |  |
| 21 | `ParseISO8601String` | `0x76F0` | 194 | UnwindData |  |
| 3 | `CopyMimeAttachmentsToMapi` | `0x8450` | 239 | UnwindData |  |
| 29 | `WriteMapiBodiesFromMimeReader` | `0x8AA0` | 55 | UnwindData |  |
| 30 | `WriteMapiBodiesFromMimeStream` | `0x9220` | 55 | UnwindData |  |
| 31 | `WriteMapiBodiesFromMimeStreamEx` | `0x9260` | 435 | UnwindData |  |
| 4 | `DownloadToVirtualStream` | `0x9C50` | 447 | UnwindData |  |
| 28 | `WriteInputStreamToNetworkStream` | `0x9ED0` | 497 | UnwindData |  |
| 32 | `CreateTemporaryFileStream` | `0xA0D0` | 47 | UnwindData |  |
| 5 | `FindMatchingNameForAddress` | `0xA520` | 787 | UnwindData |  |
| 17 | `GetSmProviderInfo` | `0xA840` | 451 | UnwindData |  |
| 18 | `GetSmRecipientType` | `0xAA10` | 47 | UnwindData |  |
| 25 | `SetSmProviderInfo` | `0xAB10` | 173 | UnwindData |  |
| 27 | `SyncNormalizePhoneNumber` | `0xABD0` | 604 | UnwindData |  |
| 6 | `GetAccountDomainForAccountAccessor` | `0xB4F0` | 164 | UnwindData |  |
| 7 | `GetAccountManagedState` | `0xB5A0` | 474 | UnwindData |  |
| 8 | `GetDataProtectionPropertyForStore` | `0xB780` | 294 | UnwindData |  |
| 9 | `GetDomainFromAccountName` | `0xB8B0` | 451 | UnwindData |  |
| 10 | `GetDomainNamesForEmailSyncList` | `0xBA80` | 425 | UnwindData |  |
| 11 | `GetDplPropertyForStore` | `0xBC30` | 276 | UnwindData |  |
| 12 | `GetIStoreForAccountGuid` | `0xBD50` | 512 | UnwindData |  |
| 15 | `GetProtectedDomainList` | `0xBF60` | 568 | UnwindData |  |
| 16 | `GetProtectionPolicyState` | `0xC1A0` | 653 | UnwindData |  |
| 19 | `IsDPLInEffect` | `0xC440` | 167 | UnwindData |  |
| 20 | `IsDomainInDelimitedList` | `0xC4F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SearchDelimitedList` | `0xC4F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SetDataProtectionPropertyForStore` | `0xC580` | 195 | UnwindData |  |
| 24 | `SetDplPropertyForStore` | `0xC650` | 192 | UnwindData |  |
| 26 | `StringCompareWithWildcard` | `0xC720` | 329 | UnwindData |  |
| 13 | `GetMimeStreamFromMMSMessage` | `0xE1C0` | 450 | UnwindData |  |
| 14 | `GetMimeStreamFromMessage` | `0xE390` | 616 | UnwindData |  |
