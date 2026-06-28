# Binary Specification: mssign32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssign32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9b9509b2c0837bcc800466a748027973f59585fc884028d9bdba93f08f1de3ba`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `FreeCryptProvFromCert` | `0x1BB0` | 93 | UnwindData |  |
| 4 | `FreeCryptProvFromCertEx` | `0x1C20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetCryptProvFromCert` | `0x1C70` | 203 | UnwindData |  |
| 6 | `GetCryptProvFromCertEx` | `0x1D50` | 206 | UnwindData |  |
| 7 | `PvkFreeCryptProv` | `0x1E30` | 43 | UnwindData |  |
| 8 | `PvkGetCryptProv` | `0x1E70` | 78 | UnwindData |  |
| 9 | `PvkPrivateKeyAcquireContext` | `0x1ED0` | 151 | UnwindData |  |
| 10 | `PvkPrivateKeyAcquireContextA` | `0x1F70` | 151 | UnwindData |  |
| 11 | `PvkPrivateKeyAcquireContextFromMemory` | `0x2010` | 106 | UnwindData |  |
| 12 | `PvkPrivateKeyAcquireContextFromMemoryA` | `0x2080` | 106 | UnwindData |  |
| 13 | `PvkPrivateKeyLoad` | `0x20F0` | 120 | UnwindData |  |
| 14 | `PvkPrivateKeyLoadA` | `0x2170` | 120 | UnwindData |  |
| 15 | `PvkPrivateKeyLoadFromMemory` | `0x21F0` | 84 | UnwindData |  |
| 16 | `PvkPrivateKeyLoadFromMemoryA` | `0x2250` | 84 | UnwindData |  |
| 17 | `PvkPrivateKeyReleaseContext` | `0x22B0` | 124 | UnwindData |  |
| 18 | `PvkPrivateKeyReleaseContextA` | `0x2340` | 124 | UnwindData |  |
| 19 | `PvkPrivateKeySave` | `0x23D0` | 53 | UnwindData |  |
| 20 | `PvkPrivateKeySaveA` | `0x2410` | 53 | UnwindData |  |
| 21 | `PvkPrivateKeySaveToMemory` | `0x2450` | 172 | UnwindData |  |
| 22 | `PvkPrivateKeySaveToMemoryA` | `0x2510` | 172 | UnwindData |  |
| 23 | `SignError` | `0x25D0` | 51 | UnwindData |  |
| 24 | `SignerAddTimeStampResponse` | `0x2610` | 40 | UnwindData |  |
| 25 | `SignerAddTimeStampResponseEx` | `0x2640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SignerCreateTimeStampRequest` | `0x2650` | 182 | UnwindData |  |
| 27 | `SignerFreeSignerContext` | `0x2710` | 59 | UnwindData |  |
| 28 | `SignerSign` | `0x2760` | 74 | UnwindData |  |
| 29 | `SignerSignEx` | `0x27B0` | 101 | UnwindData |  |
| 30 | `SignerSignEx2` | `0x2820` | 130 | UnwindData |  |
| 31 | `SignerSignEx3` | `0x28B0` | 137 | UnwindData |  |
| 32 | `SignerTimeStamp` | `0x2940` | 44 | UnwindData |  |
| 33 | `SignerTimeStampEx` | `0x2980` | 52 | UnwindData |  |
| 34 | `SignerTimeStampEx2` | `0x29C0` | 76 | UnwindData |  |
| 35 | `SignerTimeStampEx3` | `0x2A20` | 200 | UnwindData |  |
| 36 | `SpcGetCertFromKey` | `0x2AF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllRegisterServer` | `0x2B30` | 77,100 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x2B30` | 77,100 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
