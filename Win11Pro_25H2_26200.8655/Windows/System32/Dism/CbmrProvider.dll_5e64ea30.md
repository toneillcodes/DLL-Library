# Binary Specification: CbmrProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\CbmrProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5e64ea301fe3a1f17ca05fee5a2f5bf2d0835470aff724adb606850cf578c630`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x36C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x36F0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3720` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3890` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3990` | 114 | UnwindData |  |
