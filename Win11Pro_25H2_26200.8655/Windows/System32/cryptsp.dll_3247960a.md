# Binary Specification: cryptsp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3247960ae696a5e02e9ed35d2266eba6e3a15bcb24e04852bc3309306ea05700`
* **Total Exported Functions:** 65

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `CryptGetUserKey` | `0x1670` | 292 | UnwindData |  |
| 18 | `CryptGenKey` | `0x17A0` | 330 | UnwindData |  |
| 7 | `CryptDeriveKey` | `0x18F0` | 515 | UnwindData |  |
| 11 | `CryptDuplicateKey` | `0x1B00` | 480 | UnwindData |  |
| 24 | `CryptGetProvParam` | `0x1DB0` | 185 | UnwindData |  |
| 31 | `CryptSetKeyParam` | `0x1E70` | 255 | UnwindData |  |
| 39 | `CryptVerifySignatureA` | `0x1F80` | 245 | UnwindData |  |
| 10 | `CryptDuplicateHash` | `0x2080` | 628 | UnwindData |  |
| 12 | `CryptEncrypt` | `0x2460` | 365 | UnwindData |  |
| 17 | `CryptExportKey` | `0x25E0` | 354 | UnwindData |  |
| 19 | `CryptGenRandom` | `0x2750` | 108 | UnwindData |  |
| 6 | `CryptDecrypt` | `0x27D0` | 427 | UnwindData |  |
| 30 | `CryptSetHashParam` | `0x2990` | 255 | UnwindData |  |
| 9 | `CryptDestroyKey` | `0x2AA0` | 345 | UnwindData |  |
| 23 | `CryptGetKeyParam` | `0x2C00` | 252 | UnwindData |  |
| 28 | `CryptImportKey` | `0x2D60` | 684 | UnwindData |  |
| 8 | `CryptDestroyHash` | `0x3020` | 238 | UnwindData |  |
| 5 | `CryptCreateHash` | `0x3120` | 600 | UnwindData |  |
| 22 | `CryptGetHashParam` | `0x3380` | 252 | UnwindData |  |
| 26 | `CryptHashData` | `0x3490` | 318 | UnwindData |  |
| 3 | `CryptAcquireContextW` | `0x3690` | 419 | UnwindData |  |
| 2 | `CryptAcquireContextA` | `0x3840` | 3,303 | UnwindData |  |
| 21 | `CryptGetDefaultProviderW` | `0x45C0` | 467 | UnwindData |  |
| 20 | `CryptGetDefaultProviderA` | `0x47A0` | 675 | UnwindData |  |
| 29 | `CryptReleaseContext` | `0x4B70` | 530 | UnwindData |  |
| 4 | `CryptContextAddRef` | `0x51F0` | 139 | UnwindData |  |
| 16 | `CryptEnumProvidersW` | `0x5320` | 489 | UnwindData |  |
| 15 | `CryptEnumProvidersA` | `0x5510` | 922 | UnwindData |  |
| 57 | `SystemFunction024` | `0x5960` | 124 | UnwindData |  |
| 58 | `SystemFunction025` | `0x5BF0` | 152 | UnwindData |  |
| 41 | `SystemFunction006` | `0x5E20` | 257 | UnwindData |  |
| 42 | `SystemFunction007` | `0x5F30` | 298 | UnwindData |  |
| 61 | `SystemFunction030` | `0x62D0` | 35 | UnwindData |  |
| 62 | `SystemFunction031` | `0x62D0` | 35 | UnwindData |  |
| 60 | `SystemFunction027` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CryptVerifySignatureW` | `0x6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `CryptSetProvParam` | `0x6320` | 341 | UnwindData |  |
| 43 | `SystemFunction008` | `0x6480` | 221 | UnwindData |  |
| 38 | `CryptSignHashW` | `0x6590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `SystemFunction009` | `0x65A0` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `SystemFunction010` | `0x6CA0` | 95 | UnwindData |  |
| 46 | `SystemFunction011` | `0x6D10` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckSignatureInFile` | `0x75A0` | 417 | UnwindData |  |
| 65 | `SystemFunction035` | `0x75A0` | 417 | UnwindData |  |
| 13 | `CryptEnumProviderTypesA` | `0x7830` | 1,069 | UnwindData |  |
| 14 | `CryptEnumProviderTypesW` | `0x7C70` | 495 | UnwindData |  |
| 27 | `CryptHashSessionKey` | `0x7E90` | 280 | UnwindData |  |
| 33 | `CryptSetProviderA` | `0x7FB0` | 349 | UnwindData |  |
| 34 | `CryptSetProviderExA` | `0x8120` | 1,414 | UnwindData |  |
| 35 | `CryptSetProviderExW` | `0x86B0` | 204 | UnwindData |  |
| 36 | `CryptSetProviderW` | `0x8790` | 170 | UnwindData |  |
| 37 | `CryptSignHashA` | `0x8840` | 234 | UnwindData |  |
| 47 | `SystemFunction012` | `0xA8D0` | 81 | UnwindData |  |
| 48 | `SystemFunction013` | `0xA930` | 81 | UnwindData |  |
| 49 | `SystemFunction014` | `0xA990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `SystemFunction020` | `0xA990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `SystemFunction022` | `0xA990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `SystemFunction015` | `0xA9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `SystemFunction021` | `0xA9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SystemFunction023` | `0xA9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SystemFunction016` | `0xA9B0` | 80 | UnwindData |  |
| 52 | `SystemFunction018` | `0xAA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `SystemFunction026` | `0xAA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `SystemFunction032` | `0xAA30` | 90 | UnwindData |  |
| 64 | `SystemFunction033` | `0xAA30` | 90 | UnwindData |  |
