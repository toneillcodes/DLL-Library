# Binary Specification: CbsProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\CbsProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7f67c6480ae2a778174ffa5fd8eedf2f9f61f2146449dcdc2c26c0dd6adc93ff`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x5480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x54B0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x54E0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x5650` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5750` | 114 | UnwindData |  |
