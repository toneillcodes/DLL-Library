# Binary Specification: modemui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\modemui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9050ca993db5d0d4e93a49162707587bd8195f58fd31a1612d56236dac5c4ab9`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `UnimodemGetExtendedCaps` | `0x4670` | 670 | UnwindData |  |
| 12 | `InvokeControlPanel` | `0x64A0` | 184 | UnwindData |  |
| 13 | `ModemCplDlgProc` | `0x6A70` | 137 | UnwindData |  |
| 14 | `ModemPropPagesProvider` | `0x10400` | 996 | UnwindData |  |
| 8 | `UnimodemDevConfigDialog` | `0x107F0` | 56 | UnwindData |  |
| 10 | `UnimodemGetDefaultCommConfig` | `0x10830` | 303 | UnwindData |  |
| 3 | `drvCommConfigDialogA` | `0x10970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `drvGetDefaultCommConfigA` | `0x10970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `drvSetDefaultCommConfigA` | `0x10970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `drvCommConfigDialogW` | `0x10980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `drvGetDefaultCommConfigW` | `0x10990` | 112 | UnwindData |  |
| 4 | `drvSetDefaultCommConfigW` | `0x10A10` | 343 | UnwindData |  |
| 9 | `CountryRunOnce` | `0x12790` | 247 | UnwindData |  |
| 15 | `QueryModemForCountrySettings` | `0x12F40` | 2,054 | UnwindData |  |
