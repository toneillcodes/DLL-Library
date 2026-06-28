# Binary Specification: edgehtml.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\edgehtml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f41ae518dfbfad641045d1450d6de093516a68cb60fdbba1b92a11afd4ec314`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 136 | `Streams_CreateReadableStream` | `0x2D960` | 75 | UnwindData |  |
| 126 | `Streams_CreateByteChunk` | `0x3F0C90` | 123 | UnwindData |  |
| 144 | `Streams_CreateWritableStream` | `0x3F1090` | 78 | UnwindData |  |
| 120 | `InitializeLocalHtmlEngine` | `0x678B50` | 351 | UnwindData |  |
| 111 | `CreateCoreWebView` | `0x6CF660` | 121 | UnwindData |  |
| 115 | `DllEnumClassObjects` | `0x6DE710` | 269,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `DllGetClassObject` | `0x720250` | 148 | UnwindData |  |
| 119 | `GetWebPlatformObject` | `0x77FEF0` | 257,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `UninitializeLocalHtmlEngine` | `0x7BECA0` | 131 | UnwindData |  |
| 114 | `DllCanUnloadNow` | `0x7C0700` | 43 | UnwindData |  |
| 110 | `ConvertAndEscapePostData` | `0x7C4CA0` | 12 | UnwindData |  |
| 113 | `CreateHTMLPropertyPage` | `0x7C4CA0` | 12 | UnwindData |  |
| 122 | `ShowHTMLDialog` | `0x7C4CA0` | 12 | UnwindData |  |
| 123 | `ShowHTMLDialogEx` | `0x7C4CA0` | 12 | UnwindData |  |
| 124 | `ShowModalDialog` | `0x7C4CA0` | 12 | UnwindData |  |
| 125 | `ShowModelessHTMLDialog` | `0x7C4CA0` | 12 | UnwindData |  |
| 118 | `GetColorValueFromString` | `0x817800` | 102 | UnwindData |  |
| 121 | `MatchExactGetIDsOfNames` | `0x826E50` | 802,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `ClearPhishingFilterData` | `0x8EABA0` | 150 | UnwindData |  |
| 105 | *Ordinal Only* | `0xBACEA0` | 686,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | *Ordinal Only* | `0xC54940` | 76 | UnwindData |  |
| 117 | `Fetch_CreateOriginAgnosticFetch` | `0xCA39A0` | 139 | UnwindData |  |
| 127 | `Streams_CreateDefaultSizedByteChunk` | `0xCB6160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `Streams_CreateDefaultSizedWideCharChunk` | `0xCB6170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `Streams_CreateWideCharChunk` | `0xCB6180` | 89 | UnwindData |  |
| 137 | `Streams_CreateReadableStreamFromFileHandle` | `0xCB61E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `Streams_CreateReadableStreamFromFilePath` | `0xCB61F0` | 126 | UnwindData |  |
| 131 | *Ordinal Only* | `0xCFCB30` | 877,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | *Ordinal Only* | `0xDD2EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0xDD2EC0` | 254 | UnwindData |  |
| 133 | *Ordinal Only* | `0xF0E790` | 178 | UnwindData |  |
| 140 | *Ordinal Only* | `0xF0E940` | 26 | UnwindData |  |
| 141 | *Ordinal Only* | `0xF0E9E0` | 29 | UnwindData |  |
| 128 | *Ordinal Only* | `0xF0EA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | *Ordinal Only* | `0xF0EA90` | 221 | UnwindData |  |
| 139 | *Ordinal Only* | `0xF0EB80` | 120 | UnwindData |  |
| 109 | `ClearTemporaryWebDataAsync` | `0xF60D90` | 240 | UnwindData |  |
| 145 | `TravelLogCreateInstance` | `0x1055F60` | 79 | UnwindData |  |
| 134 | *Ordinal Only* | `0x10BA470` | 288 | UnwindData |  |
| 138 | *Ordinal Only* | `0x10BA5A0` | 402 | UnwindData |  |
| 107 | `CIGTestHookLoadLibraryWorkerThread` | `0x10BA740` | 55 | UnwindData |  |
| 112 | `CreateDiagnosticsToolObject` | `0x110F540` | 125 | UnwindData |  |
