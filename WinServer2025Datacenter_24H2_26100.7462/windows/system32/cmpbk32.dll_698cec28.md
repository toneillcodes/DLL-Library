# Binary Specification: cmpbk32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cmpbk32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `698cec283a3e9aefaa5689e4bacefad5bd8dcbc9d2bd1f0c8e973e1dea43f178`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PhoneBookCopyFilter` | `0x2520` | 164 | UnwindData |  |
| 2 | `PhoneBookEnumCountries` | `0x25D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PhoneBookEnumNumbers` | `0x25F0` | 78 | UnwindData |  |
| 4 | `PhoneBookEnumNumbersWithRegionsZero` | `0x2650` | 38 | UnwindData |  |
| 5 | `PhoneBookEnumRegions` | `0x2680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PhoneBookFreeFilter` | `0x26A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PhoneBookGetCountryId` | `0x26C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PhoneBookGetCountryNameA` | `0x26F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PhoneBookGetCountryNameW` | `0x2720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PhoneBookGetCurrentCountryId` | `0x2750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PhoneBookGetPhoneCanonicalA` | `0x2760` | 250 | UnwindData |  |
| 12 | `PhoneBookGetPhoneDUNA` | `0x2860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `PhoneBookGetPhoneDescA` | `0x2890` | 195 | UnwindData |  |
| 14 | `PhoneBookGetPhoneDispA` | `0x2960` | 232 | UnwindData |  |
| 15 | `PhoneBookGetPhoneNonCanonicalA` | `0x2A50` | 250 | UnwindData |  |
| 16 | `PhoneBookGetPhoneType` | `0x2B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `PhoneBookGetRegionNameA` | `0x2B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PhoneBookHasPhoneType` | `0x2BB0` | 115 | UnwindData |  |
| 20 | `PhoneBookMatchFilter` | `0x2C30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `PhoneBookParseInfoA` | `0x2C70` | 1,916 | UnwindData |  |
| 19 | `PhoneBookLoad` | `0x4F10` | 269 | UnwindData |  |
| 21 | `PhoneBookMergeChanges` | `0x5030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PhoneBookUnload` | `0x5040` | 43 | UnwindData |  |
