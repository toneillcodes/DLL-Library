# Binary Specification: cryptnet.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptnet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ad7cf4ac9616de7338de6ea5a050096ac8905583bf41c98990dc9dfc4fa64989`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `CryptRetrieveObjectByUrlW` | `0x50D0` | 2,699 | UnwindData |  |
| 17 | `I_CryptNetEnumUrlCacheEntry` | `0x9AA0` | 165 | UnwindData |  |
| 19 | `I_CryptNetGetConnectivity` | `0xD580` | 536 | UnwindData |  |
| 23 | `I_CryptNetSetUrlCachePreFetchInfo` | `0xE230` | 763 | UnwindData |  |
| 22 | `I_CryptNetSetUrlCacheFlushInfo` | `0xF630` | 388 | UnwindData |  |
| 4 | `I_CryptConvertIriToAsciiOrUnicodeWithFlags` | `0x14170` | 1,945 | UnwindData |  |
| 9 | `CryptGetTimeValidObject` | `0x17BD0` | 296 | UnwindData |  |
| 8 | `CryptGetObjectUrl` | `0x17DD0` | 258 | UnwindData |  |
| 2 | `CertDllVerifyRevocation` | `0x1B2B0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `I_CryptNetAutoFlush` | `0x1C280` | 7,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllRegisterServer` | `0x1E020` | 66 | UnwindData |  |
| 15 | `DllUnregisterServer` | `0x1E070` | 63 | UnwindData |  |
| 1 | `CertDllVerifyCTLUsage` | `0x1E0C0` | 1,001 | UnwindData |  |
| 3 | `I_CryptConvertIriToAsciiOrUnicode` | `0x1E9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `I_CryptNetGetHostNameFromUrl` | `0x1E9F0` | 132 | UnwindData |  |
| 5 | `LdapProvOpenStore` | `0x1EF40` | 194 | UnwindData |  |
| 21 | `I_CryptNetGetUserDsStoreUrl` | `0x1F450` | 553 | UnwindData |  |
| 6 | `CryptCancelAsyncRetrieval` | `0x1F790` | 29 | UnwindData |  |
| 11 | `CryptRetrieveObjectByUrlA` | `0x1F7C0` | 219 | UnwindData |  |
| 7 | `CryptFlushTimeValidObject` | `0x21890` | 196 | UnwindData |  |
| 10 | `CryptInstallCancelRetrieval` | `0x21980` | 149 | UnwindData |  |
| 13 | `CryptUninstallCancelRetrieval` | `0x21A20` | 66 | UnwindData |  |
| 18 | `I_CryptNetFlushOfflineUrl` | `0x22050` | 110 | UnwindData |  |
