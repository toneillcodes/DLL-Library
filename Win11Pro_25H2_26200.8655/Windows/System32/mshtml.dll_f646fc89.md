# Binary Specification: mshtml.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mshtml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f646fc89f1c00df50dda456278ad8aaf2d6668bd4cca79e2839939ccd96ef878`
* **Total Exported Functions:** 50

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 112 | `DllCanUnloadNow` | `0x66DE30` | 66 | UnwindData |  |
| 114 | `DllGetClassObject` | `0x679970` | 71 | UnwindData |  |
| 149 | `UninitializeLocalHtmlEngine` | `0x70A3E0` | 118,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | *Ordinal Only* | `0x727370` | 163 | UnwindData |  |
| 140 | *Ordinal Only* | `0x7E6D80` | 99 | UnwindData |  |
| 113 | `DllEnumClassObjects` | `0x7F4DA0` | 75 | UnwindData |  |
| 119 | `InitializeLocalHtmlEngine` | `0x7F4E00` | 269 | UnwindData |  |
| 108 | `ClearPhishingFilterData` | `0x7F8F60` | 85 | UnwindData |  |
| 111 | `CreateHTMLPropertyPage` | `0x7FB880` | 187 | UnwindData |  |
| 133 | `PrintHTML` | `0x980300` | 782 | UnwindData |  |
| 115 | `GetColorValueFromString` | `0x984A10` | 141 | UnwindData |  |
| 132 | `MatchExactGetIDsOfNames` | `0x9980F0` | 384 | UnwindData |  |
| 136 | `ShowHTMLDialog` | `0x9A7B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `ShowHTMLDialogEx` | `0x9A7B60` | 347 | UnwindData |  |
| 139 | `ShowModalDialog` | `0x9A7CD0` | 246 | UnwindData |  |
| 146 | `ShowModelessHTMLDialog` | `0x9A7DD0` | 157 | UnwindData |  |
| 131 | *Ordinal Only* | `0x9A7E80` | 40 | UnwindData |  |
| 116 | `GetWebPlatformObject` | `0x9B4FD0` | 95,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `ConvertAndEscapePostData` | `0x9CC360` | 247 | UnwindData |  |
| 117 | `IEIsXMLNSRegistered` | `0x9F2890` | 134 | UnwindData |  |
| 118 | `IERegisterXMLNS` | `0x9F2920` | 182 | UnwindData |  |
| 106 | *Ordinal Only* | `0xA173F0` | 76 | UnwindData |  |
| 105 | *Ordinal Only* | `0xA67A50` | 360,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | *Ordinal Only* | `0xABFB00` | 131 | UnwindData |  |
| 128 | *Ordinal Only* | `0xABFD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | *Ordinal Only* | `0xABFD20` | 77 | UnwindData |  |
| 120 | *Ordinal Only* | `0xABFD80` | 85 | UnwindData |  |
| 124 | *Ordinal Only* | `0xABFDE0` | 113 | UnwindData |  |
| 123 | *Ordinal Only* | `0xABFE60` | 85 | UnwindData |  |
| 122 | *Ordinal Only* | `0xABFEC0` | 124 | UnwindData |  |
| 127 | *Ordinal Only* | `0xABFF50` | 236 | UnwindData |  |
| 126 | *Ordinal Only* | `0xAC0050` | 336 | UnwindData |  |
| 110 | `CreateCoreWebView` | `0xACC140` | 91 | UnwindData |  |
| 129 | *Ordinal Only* | `0xAFBDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0xAFBDD0` | 252 | UnwindData |  |
| 135 | `RunHTMLApplication` | `0xB09340` | 566 | UnwindData |  |
| 147 | `TravelLogCreateInstance` | `0x1066C80` | 108 | UnwindData |  |
| 148 | `TravelLogStgCreateInstance` | `0x1067310` | 175 | UnwindData |  |
| 104 | *Ordinal Only* | `0x1099C40` | 108 | UnwindData |  |
| 100 | *Ordinal Only* | `0x1099CC0` | 182 | UnwindData |  |
| 101 | *Ordinal Only* | `0x1099D80` | 162 | UnwindData |  |
| 102 | *Ordinal Only* | `0x1099E30` | 4,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x109AFE0` | 1,089 | UnwindData |  |
| 134 | *Ordinal Only* | `0x10A05C0` | 288 | UnwindData |  |
| 138 | *Ordinal Only* | `0x10A06F0` | 402 | UnwindData |  |
| 145 | *Ordinal Only* | `0x10AD8C0` | 269 | UnwindData |  |
| 142 | *Ordinal Only* | `0x10ADF70` | 131 | UnwindData |  |
| 144 | *Ordinal Only* | `0x10AE130` | 259 | UnwindData |  |
| 143 | *Ordinal Only* | `0x10AE240` | 51 | UnwindData |  |
| 141 | *Ordinal Only* | `0x10AE560` | 652 | UnwindData |  |
