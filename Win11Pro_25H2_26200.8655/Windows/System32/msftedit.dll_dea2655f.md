# Binary Specification: msftedit.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msftedit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dea2655f6f7f7cd4a89bac75ece47056761010f975f9b8b9cb8cfaff8286789c`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateTextServices` | `0xFFBF0` | 149 | UnwindData |  |
| 35 | `ShutdownTextServices` | `0x1247E0` | 232 | UnwindData |  |
| 13 | `RichEditWndProc` | `0x124E70` | 2,931 | UnwindData |  |
| 8 | `DisableOleinitCheck` | `0x13CFD0` | 39 | UnwindData |  |
| 11 | `SetCustomTextOutHandlerEx` | `0x13D000` | 97 | UnwindData |  |
| 36 | `SetTextServicesDpiCalculationOverride` | `0x13D070` | 185 | UnwindData |  |
| 22 | `GetMathAlphanumeric` | `0x1BE070` | 942 | UnwindData |  |
| 21 | `GetMathAlphanumericCode` | `0x1BE430` | 591 | UnwindData |  |
| 18 | `MathBuildDown` | `0x1C6A80` | 165 | UnwindData |  |
| 17 | `MathBuildUp` | `0x1C6B30` | 767 | UnwindData |  |
| 19 | `MathTranslate` | `0x1C6E40` | 734 | UnwindData |  |
| 26 | `DllGetActivationFactory` | `0x1E7300` | 45 | UnwindData |  |
| 10 | `RichEdit10ANSIWndProc` | `0x203350` | 254 | UnwindData |  |
| 9 | `RichEditANSIWndProc` | `0x203460` | 145 | UnwindData |  |
| 12 | `DllGetVersion` | `0x203DB0` | 154 | UnwindData |  |
| 24 | `IID_ITextDocument2` | `0x2AE1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `IID_ITextServices2` | `0x2AE1C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IID_ITextServices` | `0x2AE210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IID_IRichEditOle` | `0x2AE230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IID_IRichEditOleCallback` | `0x2AE240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `IID_IRicheditWindowlessAccessibility` | `0x2AE270` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `IID_ITextHost2` | `0x2AE2E8` | 11,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `IID_IRicheditUiaNotificationOverrides` | `0x2B11C0` | 8,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IID_ITextHost` | `0x2B34D8` | 18,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `IID_IRicheditUiaOverrides` | `0x2B7E38` | 0 | Indeterminate |  |
