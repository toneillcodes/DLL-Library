# Binary Specification: edgehtml.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\edgehtml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `56351c61efe8934a496a96f589dadab485d82fb3e4a6bd3d47f378fa1d5e8b65`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 136 | `Streams_CreateReadableStream` | `0x2D930` | 75 | UnwindData |  |
| 126 | `Streams_CreateByteChunk` | `0x477C50` | 123 | UnwindData |  |
| 144 | `Streams_CreateWritableStream` | `0x478050` | 78 | UnwindData |  |
| 120 | `InitializeLocalHtmlEngine` | `0x678950` | 351 | UnwindData |  |
| 111 | `CreateCoreWebView` | `0x6CFC10` | 121 | UnwindData |  |
| 115 | `DllEnumClassObjects` | `0x6DF020` | 266,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `DllGetClassObject` | `0x7200A0` | 148 | UnwindData |  |
| 119 | `GetWebPlatformObject` | `0x77F9D0` | 257,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `UninitializeLocalHtmlEngine` | `0x7BE620` | 131 | UnwindData |  |
| 114 | `DllCanUnloadNow` | `0x7C0080` | 43 | UnwindData |  |
| 110 | `ConvertAndEscapePostData` | `0x7C4370` | 12 | UnwindData |  |
| 113 | `CreateHTMLPropertyPage` | `0x7C4370` | 12 | UnwindData |  |
| 122 | `ShowHTMLDialog` | `0x7C4370` | 12 | UnwindData |  |
| 123 | `ShowHTMLDialogEx` | `0x7C4370` | 12 | UnwindData |  |
| 124 | `ShowModalDialog` | `0x7C4370` | 12 | UnwindData |  |
| 125 | `ShowModelessHTMLDialog` | `0x7C4370` | 12 | UnwindData |  |
| 118 | `GetColorValueFromString` | `0x818010` | 102 | UnwindData |  |
| 121 | `MatchExactGetIDsOfNames` | `0x827660` | 801,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `ClearPhishingFilterData` | `0x8EAFD0` | 150 | UnwindData |  |
| 105 | *Ordinal Only* | `0xBACF70` | 686,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | *Ordinal Only* | `0xC548C0` | 76 | UnwindData |  |
| 117 | `Fetch_CreateOriginAgnosticFetch` | `0xCA3840` | 139 | UnwindData |  |
| 127 | `Streams_CreateDefaultSizedByteChunk` | `0xCB5FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `Streams_CreateDefaultSizedWideCharChunk` | `0xCB6000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `Streams_CreateWideCharChunk` | `0xCB6010` | 89 | UnwindData |  |
| 137 | `Streams_CreateReadableStreamFromFileHandle` | `0xCB6070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `Streams_CreateReadableStreamFromFilePath` | `0xCB6080` | 126 | UnwindData |  |
| 131 | *Ordinal Only* | `0xCFC9C0` | 877,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | *Ordinal Only* | `0xDD2D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0xDD2D40` | 254 | UnwindData |  |
| 133 | *Ordinal Only* | `0xF0DAE0` | 178 | UnwindData |  |
| 140 | *Ordinal Only* | `0xF0DC90` | 26 | UnwindData |  |
| 141 | *Ordinal Only* | `0xF0DD30` | 29 | UnwindData |  |
| 128 | *Ordinal Only* | `0xF0DDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | *Ordinal Only* | `0xF0DDE0` | 221 | UnwindData |  |
| 139 | *Ordinal Only* | `0xF0DED0` | 120 | UnwindData |  |
| 109 | `ClearTemporaryWebDataAsync` | `0xF5FF40` | 240 | UnwindData |  |
| 145 | `TravelLogCreateInstance` | `0x1055DC0` | 79 | UnwindData |  |
| 134 | *Ordinal Only* | `0x10BA1A0` | 288 | UnwindData |  |
| 138 | *Ordinal Only* | `0x10BA2D0` | 402 | UnwindData |  |
| 107 | `CIGTestHookLoadLibraryWorkerThread` | `0x10BA470` | 55 | UnwindData |  |
| 112 | `CreateDiagnosticsToolObject` | `0x110F190` | 125 | UnwindData |  |
