# Binary Specification: cryptsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bea87cf35a0d6c87286f5d7f55d9bdf6d7de084260e0167621f0ca666e60bea7`
* **Total Exported Functions:** 65

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `CryptGetUserKey` | `0x16B0` | 292 | UnwindData |  |
| 18 | `CryptGenKey` | `0x17E0` | 330 | UnwindData |  |
| 7 | `CryptDeriveKey` | `0x1930` | 515 | UnwindData |  |
| 11 | `CryptDuplicateKey` | `0x1B40` | 480 | UnwindData |  |
| 24 | `CryptGetProvParam` | `0x1DF0` | 185 | UnwindData |  |
| 31 | `CryptSetKeyParam` | `0x1EB0` | 255 | UnwindData |  |
| 39 | `CryptVerifySignatureA` | `0x1FC0` | 245 | UnwindData |  |
| 10 | `CryptDuplicateHash` | `0x20C0` | 628 | UnwindData |  |
| 12 | `CryptEncrypt` | `0x24A0` | 365 | UnwindData |  |
| 17 | `CryptExportKey` | `0x2620` | 354 | UnwindData |  |
| 19 | `CryptGenRandom` | `0x2790` | 108 | UnwindData |  |
| 6 | `CryptDecrypt` | `0x2810` | 427 | UnwindData |  |
| 30 | `CryptSetHashParam` | `0x29D0` | 255 | UnwindData |  |
| 9 | `CryptDestroyKey` | `0x2AE0` | 345 | UnwindData |  |
| 23 | `CryptGetKeyParam` | `0x2C40` | 252 | UnwindData |  |
| 28 | `CryptImportKey` | `0x2DA0` | 684 | UnwindData |  |
| 8 | `CryptDestroyHash` | `0x3060` | 238 | UnwindData |  |
| 5 | `CryptCreateHash` | `0x3160` | 600 | UnwindData |  |
| 22 | `CryptGetHashParam` | `0x33C0` | 252 | UnwindData |  |
| 26 | `CryptHashData` | `0x34D0` | 318 | UnwindData |  |
| 3 | `CryptAcquireContextW` | `0x36D0` | 419 | UnwindData |  |
| 2 | `CryptAcquireContextA` | `0x3880` | 3,303 | UnwindData |  |
| 21 | `CryptGetDefaultProviderW` | `0x4600` | 467 | UnwindData |  |
| 20 | `CryptGetDefaultProviderA` | `0x47E0` | 675 | UnwindData |  |
| 29 | `CryptReleaseContext` | `0x4BB0` | 530 | UnwindData |  |
| 4 | `CryptContextAddRef` | `0x52A0` | 139 | UnwindData |  |
| 16 | `CryptEnumProvidersW` | `0x53D0` | 489 | UnwindData |  |
| 15 | `CryptEnumProvidersA` | `0x55C0` | 922 | UnwindData |  |
| 57 | `SystemFunction024` | `0x5A10` | 124 | UnwindData |  |
| 58 | `SystemFunction025` | `0x5CA0` | 152 | UnwindData |  |
| 41 | `SystemFunction006` | `0x5ED0` | 257 | UnwindData |  |
| 42 | `SystemFunction007` | `0x5FE0` | 298 | UnwindData |  |
| 61 | `SystemFunction030` | `0x6380` | 35 | UnwindData |  |
| 62 | `SystemFunction031` | `0x6380` | 35 | UnwindData |  |
| 60 | `SystemFunction027` | `0x63B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CryptVerifySignatureW` | `0x63C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `CryptSetProvParam` | `0x63D0` | 341 | UnwindData |  |
| 43 | `SystemFunction008` | `0x6530` | 221 | UnwindData |  |
| 38 | `CryptSignHashW` | `0x6640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `SystemFunction009` | `0x6650` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `SystemFunction010` | `0x6D60` | 95 | UnwindData |  |
| 46 | `SystemFunction011` | `0x6DD0` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckSignatureInFile` | `0x7660` | 417 | UnwindData |  |
| 65 | `SystemFunction035` | `0x7660` | 417 | UnwindData |  |
| 13 | `CryptEnumProviderTypesA` | `0x78F0` | 1,069 | UnwindData |  |
| 14 | `CryptEnumProviderTypesW` | `0x7D30` | 495 | UnwindData |  |
| 27 | `CryptHashSessionKey` | `0x7F50` | 280 | UnwindData |  |
| 33 | `CryptSetProviderA` | `0x8070` | 349 | UnwindData |  |
| 34 | `CryptSetProviderExA` | `0x81E0` | 1,414 | UnwindData |  |
| 35 | `CryptSetProviderExW` | `0x8770` | 204 | UnwindData |  |
| 36 | `CryptSetProviderW` | `0x8850` | 170 | UnwindData |  |
| 37 | `CryptSignHashA` | `0x8900` | 234 | UnwindData |  |
| 47 | `SystemFunction012` | `0xA990` | 81 | UnwindData |  |
| 48 | `SystemFunction013` | `0xA9F0` | 81 | UnwindData |  |
| 49 | `SystemFunction014` | `0xAA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `SystemFunction020` | `0xAA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `SystemFunction022` | `0xAA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `SystemFunction015` | `0xAA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `SystemFunction021` | `0xAA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SystemFunction023` | `0xAA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SystemFunction016` | `0xAA70` | 80 | UnwindData |  |
| 52 | `SystemFunction018` | `0xAAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `SystemFunction026` | `0xAAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `SystemFunction032` | `0xAAF0` | 90 | UnwindData |  |
| 64 | `SystemFunction033` | `0xAAF0` | 90 | UnwindData |  |
