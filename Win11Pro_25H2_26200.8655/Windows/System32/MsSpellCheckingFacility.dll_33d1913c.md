# Binary Specification: MsSpellCheckingFacility.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MsSpellCheckingFacility.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `33d1913c556cdb1f4f393b0548abd4b250b45edabfecca4fcae524e382062e34`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `SpellerCheck` | `0x23550` | 973 | UnwindData |  |
| 10 | `SpellerOpenLex` | `0x25760` | 1,568 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x29500` | 86 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x2B010` | 56 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4BD60` | 45 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4BDA0` | 76 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4BE00` | 263,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SpellerCloseLex` | `0x8C220` | 274 | UnwindData |  |
| 8 | `SpellerGetOptions` | `0x8C680` | 581 | UnwindData |  |
| 9 | `SpellerInit` | `0x8C980` | 77 | UnwindData |  |
| 11 | `SpellerSetOptions` | `0x8C9E0` | 697 | UnwindData |  |
| 12 | `SpellerTerminate` | `0x8CCA0` | 39 | UnwindData |  |
