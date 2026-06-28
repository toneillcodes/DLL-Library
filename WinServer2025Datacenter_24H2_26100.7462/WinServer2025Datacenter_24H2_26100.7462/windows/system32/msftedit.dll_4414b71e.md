# Binary Specification: msftedit.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msftedit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4414b71ed17f138b575175fa357087911dccb8a7fc6caea4b00299190dbf8881`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateTextServices` | `0xFFCB0` | 149 | UnwindData |  |
| 35 | `ShutdownTextServices` | `0x1246E0` | 232 | UnwindData |  |
| 13 | `RichEditWndProc` | `0x125000` | 2,931 | UnwindData |  |
| 8 | `DisableOleinitCheck` | `0x13D0B0` | 39 | UnwindData |  |
| 11 | `SetCustomTextOutHandlerEx` | `0x13D0E0` | 97 | UnwindData |  |
| 36 | `SetTextServicesDpiCalculationOverride` | `0x13D150` | 185 | UnwindData |  |
| 22 | `GetMathAlphanumeric` | `0x1BED30` | 942 | UnwindData |  |
| 21 | `GetMathAlphanumericCode` | `0x1BF0F0` | 591 | UnwindData |  |
| 18 | `MathBuildDown` | `0x1C7740` | 165 | UnwindData |  |
| 17 | `MathBuildUp` | `0x1C77F0` | 767 | UnwindData |  |
| 19 | `MathTranslate` | `0x1C7B00` | 734 | UnwindData |  |
| 26 | `DllGetActivationFactory` | `0x1E7FC0` | 45 | UnwindData |  |
| 10 | `RichEdit10ANSIWndProc` | `0x203FD0` | 254 | UnwindData |  |
| 9 | `RichEditANSIWndProc` | `0x2040E0` | 145 | UnwindData |  |
| 12 | `DllGetVersion` | `0x204A30` | 154 | UnwindData |  |
| 24 | `IID_ITextDocument2` | `0x2AF1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `IID_ITextServices2` | `0x2AF1C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IID_ITextServices` | `0x2AF210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IID_IRichEditOle` | `0x2AF230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IID_IRichEditOleCallback` | `0x2AF240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `IID_IRicheditWindowlessAccessibility` | `0x2AF270` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `IID_ITextHost2` | `0x2AF2E8` | 11,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `IID_IRicheditUiaNotificationOverrides` | `0x2B21C0` | 8,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IID_ITextHost` | `0x2B44D8` | 18,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `IID_IRicheditUiaOverrides` | `0x2B8E48` | 0 | Indeterminate |  |
