# Binary Specification: input.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\input.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6ac10560c94bd5260a5468f68e901f2b36879e9c53011cbc4cc60915fe355de8`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 200 | `InputDll_DownlevelInitialize` | `0xA940` | 75,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `ActivateInputProfile` | `0x1CF60` | 109 | UnwindData |  |
| 110 | `EnumEnabledLayoutOrTip` | `0x1CFE0` | 1,369 | UnwindData |  |
| 118 | `EnumEnabledLayoutOrTipPrivate` | `0x1D540` | 141 | UnwindData |  |
| 108 | `EnumLayoutOrTipForSetup` | `0x1D5E0` | 203 | UnwindData |  |
| 113 | `GetDefaultLayout` | `0x1D6C0` | 1,177 | UnwindData |  |
| 121 | `GetEnabledInputMethods` | `0x1DB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | *Ordinal Only* | `0x1DB70` | 640 | UnwindData |  |
| 114 | `GetLayoutDescription` | `0x1DE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1DE10` | 124 | UnwindData |  |
| 104 | `InstallLayoutOrTip` | `0x1DEA0` | 219 | UnwindData |  |
| 120 | `InstallLayoutOrTipOffline` | `0x1DF90` | 97 | UnwindData |  |
| 117 | `InstallLayoutOrTipPrivate` | `0x1E000` | 284 | UnwindData |  |
| 109 | `InstallLayoutOrTipUserReg` | `0x1E130` | 269 | UnwindData |  |
| 115 | *Ordinal Only* | `0x1E250` | 818 | UnwindData |  |
| 111 | `QueryLayoutOrTipString` | `0x1E590` | 29 | UnwindData |  |
| 112 | `QueryLayoutOrTipStringUserReg` | `0x1E5C0` | 598 | UnwindData |  |
| 105 | `SaveDefaultUserInputSettings` | `0x1E820` | 334 | UnwindData |  |
| 106 | `SaveSystemAcctInputSettings` | `0x1E980` | 1,191 | UnwindData |  |
| 107 | `SetDefaultLayoutOrTip` | `0x1EE30` | 316 | UnwindData |  |
| 103 | *Ordinal Only* | `0x1F960` | 112 | UnwindData |  |
| 100 | `CPlApplet` | `0x21770` | 251 | UnwindData |  |
| 203 | `InputDll_DownlevelEnumLayoutOrTipForSetup` | `0x23D00` | 281 | UnwindData |  |
| 201 | `InputDll_DownlevelSetUILanguage` | `0x23E20` | 215 | UnwindData |  |
| 202 | `InputDll_DownlevelUninitialize` | `0x23F00` | 44 | UnwindData |  |
