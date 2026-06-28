# Binary Specification: input.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\input.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4b31f60de50a38e5e80e3bdffdd0e17f561e812b6e8d91ec88607fcb62c56afc`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 200 | `InputDll_DownlevelInitialize` | `0xAAA0` | 73,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `ActivateInputProfile` | `0x1CAA0` | 109 | UnwindData |  |
| 110 | `EnumEnabledLayoutOrTip` | `0x1CB20` | 1,369 | UnwindData |  |
| 118 | `EnumEnabledLayoutOrTipPrivate` | `0x1D080` | 141 | UnwindData |  |
| 108 | `EnumLayoutOrTipForSetup` | `0x1D120` | 203 | UnwindData |  |
| 113 | `GetDefaultLayout` | `0x1D200` | 1,177 | UnwindData |  |
| 121 | `GetEnabledInputMethods` | `0x1D6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | *Ordinal Only* | `0x1D6B0` | 640 | UnwindData |  |
| 114 | `GetLayoutDescription` | `0x1D940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1D950` | 124 | UnwindData |  |
| 104 | `InstallLayoutOrTip` | `0x1D9E0` | 219 | UnwindData |  |
| 120 | `InstallLayoutOrTipOffline` | `0x1DAD0` | 97 | UnwindData |  |
| 117 | `InstallLayoutOrTipPrivate` | `0x1DB40` | 187 | UnwindData |  |
| 109 | `InstallLayoutOrTipUserReg` | `0x1DC10` | 269 | UnwindData |  |
| 115 | *Ordinal Only* | `0x1DD30` | 818 | UnwindData |  |
| 111 | `QueryLayoutOrTipString` | `0x1E070` | 29 | UnwindData |  |
| 112 | `QueryLayoutOrTipStringUserReg` | `0x1E0A0` | 598 | UnwindData |  |
| 105 | `SaveDefaultUserInputSettings` | `0x1E300` | 334 | UnwindData |  |
| 106 | `SaveSystemAcctInputSettings` | `0x1E460` | 1,191 | UnwindData |  |
| 107 | `SetDefaultLayoutOrTip` | `0x1E910` | 316 | UnwindData |  |
| 103 | *Ordinal Only* | `0x1F440` | 112 | UnwindData |  |
| 100 | `CPlApplet` | `0x21530` | 251 | UnwindData |  |
| 203 | `InputDll_DownlevelEnumLayoutOrTipForSetup` | `0x23AC0` | 281 | UnwindData |  |
| 201 | `InputDll_DownlevelSetUILanguage` | `0x23BE0` | 215 | UnwindData |  |
| 202 | `InputDll_DownlevelUninitialize` | `0x23CC0` | 44 | UnwindData |  |
