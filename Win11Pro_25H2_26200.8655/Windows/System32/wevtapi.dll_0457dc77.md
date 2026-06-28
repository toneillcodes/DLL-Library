# Binary Specification: wevtapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wevtapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0457dc77636c62433c282eea6c955f7cd1c8c9a68de59a908feedff2daaa3691`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `EvtIntReportAuthzEventAndSourceAsync` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EvtIntReportAuthzEventAndSourceAsync` |
| 25 | `EvtIntReportEventAndSourceAsync` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EvtIntReportEventAndSourceAsync` |
| 37 | `EvtOpenPublisherMetadata` | `0x1810` | 862 | UnwindData |  |
| 10 | `EvtGetChannelConfigProperty` | `0x90B0` | 385 | UnwindData |  |
| 40 | `EvtRender` | `0x9240` | 1,288 | UnwindData |  |
| 7 | `EvtCreateRenderContext` | `0x9E80` | 721 | UnwindData |  |
| 9 | `EvtFormatMessage` | `0xA160` | 1,138 | UnwindData |  |
| 28 | `EvtNext` | `0xA5E0` | 599 | UnwindData |  |
| 5 | `EvtClose` | `0xB060` | 448 | UnwindData |  |
| 8 | `EvtExportLog` | `0x107F0` | 759 | UnwindData |  |
| 32 | `EvtOpenChannelConfig` | `0x13190` | 501 | UnwindData |  |
| 35 | `EvtOpenLog` | `0x14350` | 727 | UnwindData |  |
| 44 | `EvtSubscribe` | `0x150D0` | 1,351 | UnwindData |  |
| 39 | `EvtQuery` | `0x16070` | 779 | UnwindData |  |
| 16 | `EvtGetObjectArraySize` | `0x16C80` | 160 | UnwindData |  |
| 42 | `EvtSeek` | `0x16D30` | 574 | UnwindData |  |
| 31 | `EvtNextPublisherId` | `0x17000` | 180 | UnwindData |  |
| 45 | `EvtUpdateBookmark` | `0x17160` | 193 | UnwindData |  |
| 14 | `EvtGetLogInfo` | `0x173A0` | 226 | UnwindData |  |
| 29 | `EvtNextChannelPath` | `0x17520` | 180 | UnwindData |  |
| 15 | `EvtGetObjectArrayProperty` | `0x17AC0` | 309 | UnwindData |  |
| 17 | `EvtGetPublisherMetadataProperty` | `0x18870` | 330 | UnwindData |  |
| 30 | `EvtNextEventMetadata` | `0x189C0` | 449 | UnwindData |  |
| 11 | `EvtGetEventInfo` | `0x18FE0` | 217 | UnwindData |  |
| 6 | `EvtCreateBookmark` | `0x1DC00` | 179 | UnwindData |  |
| 19 | `EvtIntAssertConfig` | `0x1E4C0` | 361 | UnwindData |  |
| 12 | `EvtGetEventMetadataProperty` | `0x1EA90` | 319 | UnwindData |  |
| 36 | `EvtOpenPublisherEnum` | `0x1F6F0` | 439 | UnwindData |  |
| 38 | `EvtOpenSession` | `0x1FA30` | 449 | UnwindData |  |
| 34 | `EvtOpenEventMetadataEnum` | `0x1FC20` | 314 | UnwindData |  |
| 18 | `EvtGetQueryInfo` | `0x21920` | 952 | UnwindData |  |
| 2 | `EvtArchiveExportedLog` | `0x23F00` | 502 | UnwindData |  |
| 3 | `EvtCancel` | `0x24100` | 157 | UnwindData |  |
| 4 | `EvtClearLog` | `0x241B0` | 394 | UnwindData |  |
| 13 | `EvtGetExtendedStatus` | `0x24340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EvtOpenChannelEnum` | `0x24360` | 437 | UnwindData |  |
| 41 | `EvtSaveChannelConfig` | `0x24520` | 222 | UnwindData |  |
| 43 | `EvtSetChannelConfigProperty` | `0x24610` | 273 | UnwindData |  |
| 1 | `EvtIntSysprepCleanup` | `0x24870` | 151 | UnwindData |  |
| 20 | `EvtIntCreateBinXMLFromCustomXML` | `0x24A40` | 65 | UnwindData |  |
| 21 | `EvtIntCreateLocalLogfile` | `0x24A90` | 257 | UnwindData |  |
| 22 | `EvtIntGetClassicLogDisplayName` | `0x24BA0` | 963 | UnwindData |  |
| 23 | `EvtIntRenderResourceEventTemplate` | `0x24F70` | 1,306 | UnwindData |  |
| 26 | `EvtIntRetractConfig` | `0x25490` | 343 | UnwindData |  |
| 27 | `EvtIntWriteXmlEventToLocalLogfile` | `0x255F0` | 626 | UnwindData |  |
