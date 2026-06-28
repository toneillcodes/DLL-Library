# Binary Specification: mshtml.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mshtml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f211cc63fd4adf900202ed33014b87d54b2cd90e5bfd9ba92c627909b7670101`
* **Total Exported Functions:** 50

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 112 | `DllCanUnloadNow` | `0x6727D0` | 66 | UnwindData |  |
| 114 | `DllGetClassObject` | `0x67D0F0` | 71 | UnwindData |  |
| 149 | `UninitializeLocalHtmlEngine` | `0x70B7F0` | 115,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | *Ordinal Only* | `0x727A40` | 163 | UnwindData |  |
| 140 | *Ordinal Only* | `0x7E7120` | 99 | UnwindData |  |
| 113 | `DllEnumClassObjects` | `0x7F50A0` | 75 | UnwindData |  |
| 119 | `InitializeLocalHtmlEngine` | `0x7F5100` | 269 | UnwindData |  |
| 108 | `ClearPhishingFilterData` | `0x7F9150` | 85 | UnwindData |  |
| 111 | `CreateHTMLPropertyPage` | `0x7FE540` | 187 | UnwindData |  |
| 133 | `PrintHTML` | `0x985330` | 782 | UnwindData |  |
| 115 | `GetColorValueFromString` | `0x989A40` | 141 | UnwindData |  |
| 132 | `MatchExactGetIDsOfNames` | `0x99D120` | 384 | UnwindData |  |
| 136 | `ShowHTMLDialog` | `0x9ACB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `ShowHTMLDialogEx` | `0x9ACB90` | 347 | UnwindData |  |
| 139 | `ShowModalDialog` | `0x9ACD00` | 246 | UnwindData |  |
| 146 | `ShowModelessHTMLDialog` | `0x9ACE00` | 157 | UnwindData |  |
| 131 | *Ordinal Only* | `0x9ACEB0` | 40 | UnwindData |  |
| 116 | `GetWebPlatformObject` | `0x9BA000` | 95,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `ConvertAndEscapePostData` | `0x9D1390` | 247 | UnwindData |  |
| 117 | `IEIsXMLNSRegistered` | `0x9F78C0` | 134 | UnwindData |  |
| 118 | `IERegisterXMLNS` | `0x9F7950` | 182 | UnwindData |  |
| 106 | *Ordinal Only* | `0xA1C420` | 76 | UnwindData |  |
| 105 | *Ordinal Only* | `0xA6CA80` | 360,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | *Ordinal Only* | `0xAC4B30` | 131 | UnwindData |  |
| 128 | *Ordinal Only* | `0xAC4D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | *Ordinal Only* | `0xAC4D50` | 77 | UnwindData |  |
| 120 | *Ordinal Only* | `0xAC4DB0` | 85 | UnwindData |  |
| 124 | *Ordinal Only* | `0xAC4E10` | 113 | UnwindData |  |
| 123 | *Ordinal Only* | `0xAC4E90` | 85 | UnwindData |  |
| 122 | *Ordinal Only* | `0xAC4EF0` | 124 | UnwindData |  |
| 127 | *Ordinal Only* | `0xAC4F80` | 236 | UnwindData |  |
| 126 | *Ordinal Only* | `0xAC5080` | 336 | UnwindData |  |
| 110 | `CreateCoreWebView` | `0xAD11B0` | 91 | UnwindData |  |
| 129 | *Ordinal Only* | `0xB00CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0xB00CC0` | 252 | UnwindData |  |
| 135 | `RunHTMLApplication` | `0xB0E230` | 566 | UnwindData |  |
| 147 | `TravelLogCreateInstance` | `0x106CD90` | 108 | UnwindData |  |
| 148 | `TravelLogStgCreateInstance` | `0x106D420` | 175 | UnwindData |  |
| 104 | *Ordinal Only* | `0x10A0890` | 108 | UnwindData |  |
| 100 | *Ordinal Only* | `0x10A0910` | 182 | UnwindData |  |
| 101 | *Ordinal Only* | `0x10A09D0` | 162 | UnwindData |  |
| 102 | *Ordinal Only* | `0x10A0A80` | 4,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x10A1C30` | 1,089 | UnwindData |  |
| 134 | *Ordinal Only* | `0x10A7210` | 288 | UnwindData |  |
| 138 | *Ordinal Only* | `0x10A7340` | 402 | UnwindData |  |
| 145 | *Ordinal Only* | `0x10B4510` | 269 | UnwindData |  |
| 142 | *Ordinal Only* | `0x10B4BC0` | 131 | UnwindData |  |
| 144 | *Ordinal Only* | `0x10B4D80` | 259 | UnwindData |  |
| 143 | *Ordinal Only* | `0x10B4E90` | 51 | UnwindData |  |
| 141 | *Ordinal Only* | `0x10B51B0` | 652 | UnwindData |  |
