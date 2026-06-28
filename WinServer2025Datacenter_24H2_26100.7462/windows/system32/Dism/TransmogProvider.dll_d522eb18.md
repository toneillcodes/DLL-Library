# Binary Specification: TransmogProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\TransmogProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d522eb182b1875e541740738bfc4edfa7111daefc10a411065c358a909712246`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x22150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x22180` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x221B0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x22320` | 304 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x22460` | 166 | UnwindData |  |
