# Binary Specification: IMJPLMP.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\IMEJP\IMJPLMP.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `752d3b30b5d32ff0b53bb86cb74ba5946ba8da04566750c9b09e1f6fe70afa58`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `IMECFM_AddJpnWordInfoAndLmContextForWatsonReport` | `0x34B50` | 281 | UnwindData |  |
| 1 | `CJDictsCommentDictionary_CreateInstance` | `0x36620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CJDictsDataForDWORD_CreateInstance` | `0x36630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CJDictsDictionaryManifest_CreateInstance` | `0x36640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CJDictsIndexerSatori_CreateInstance` | `0x36650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CJDictsSystemLexiconStoreDelayLoad__CreateInstance` | `0x36660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CJDictsUserDictionary_CreateInstance` | `0x36670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CJDictsUserDictionary_FillByDummyHeader` | `0x36680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllCanUnloadNow` | `0x36690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x366B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllRegisterServer` | `0x36750` | 43 | UnwindData |  |
| 11 | `DllUnregisterServer` | `0x36790` | 60 | UnwindData |  |
| 12 | `GetSegmentedStr` | `0x367E0` | 164 | UnwindData |  |
| 14 | `InitGetSegmentedStr` | `0x36890` | 625 | UnwindData |  |
| 15 | `UnInitGetSegmentedStr` | `0x36B10` | 38 | UnwindData |  |
