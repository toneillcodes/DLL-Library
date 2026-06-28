# Binary Specification: MsSpellCheckingFacility.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MsSpellCheckingFacility.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `261b4907caa504ac8750a1db80eecd142c26c6d1319809d0eab1effde482df99`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `SpellerCheck` | `0x23540` | 973 | UnwindData |  |
| 10 | `SpellerOpenLex` | `0x25750` | 1,568 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x294F0` | 86 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x2B000` | 56 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4BC30` | 45 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4BC70` | 76 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4BCD0` | 262,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SpellerCloseLex` | `0x8BF50` | 274 | UnwindData |  |
| 8 | `SpellerGetOptions` | `0x8C3B0` | 581 | UnwindData |  |
| 9 | `SpellerInit` | `0x8C6B0` | 77 | UnwindData |  |
| 11 | `SpellerSetOptions` | `0x8C710` | 697 | UnwindData |  |
| 12 | `SpellerTerminate` | `0x8C9D0` | 39 | UnwindData |  |
