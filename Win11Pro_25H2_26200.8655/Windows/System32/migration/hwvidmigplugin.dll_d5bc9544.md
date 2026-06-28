# Binary Specification: hwvidmigplugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\hwvidmigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5bc954426fb981266b5d21362c52bba113149c4372a1ce3315bd8e7e7ec7ca0`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5360` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5390` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x54D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x54F0` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5620` | 151 | UnwindData |  |
