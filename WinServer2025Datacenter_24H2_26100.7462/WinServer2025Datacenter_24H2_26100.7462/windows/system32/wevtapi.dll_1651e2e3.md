# Binary Specification: wevtapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wevtapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1651e2e33615d9ef80e8e9578b949454b259080ab7bb756d7d695b80988fe0a7`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `EvtIntReportAuthzEventAndSourceAsync` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EvtIntReportAuthzEventAndSourceAsync` |
| 25 | `EvtIntReportEventAndSourceAsync` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EvtIntReportEventAndSourceAsync` |
| 37 | `EvtOpenPublisherMetadata` | `0x1630` | 862 | UnwindData |  |
| 10 | `EvtGetChannelConfigProperty` | `0x8ED0` | 385 | UnwindData |  |
| 40 | `EvtRender` | `0x9060` | 1,288 | UnwindData |  |
| 7 | `EvtCreateRenderContext` | `0x9CA0` | 721 | UnwindData |  |
| 9 | `EvtFormatMessage` | `0x9F80` | 1,138 | UnwindData |  |
| 28 | `EvtNext` | `0xA400` | 599 | UnwindData |  |
| 5 | `EvtClose` | `0xAE80` | 448 | UnwindData |  |
| 8 | `EvtExportLog` | `0x10610` | 759 | UnwindData |  |
| 32 | `EvtOpenChannelConfig` | `0x12FB0` | 501 | UnwindData |  |
| 35 | `EvtOpenLog` | `0x14170` | 727 | UnwindData |  |
| 44 | `EvtSubscribe` | `0x14EF0` | 1,351 | UnwindData |  |
| 39 | `EvtQuery` | `0x15E90` | 779 | UnwindData |  |
| 16 | `EvtGetObjectArraySize` | `0x16AA0` | 160 | UnwindData |  |
| 42 | `EvtSeek` | `0x16B50` | 574 | UnwindData |  |
| 31 | `EvtNextPublisherId` | `0x16E20` | 180 | UnwindData |  |
| 45 | `EvtUpdateBookmark` | `0x16F80` | 193 | UnwindData |  |
| 14 | `EvtGetLogInfo` | `0x171C0` | 226 | UnwindData |  |
| 29 | `EvtNextChannelPath` | `0x17340` | 180 | UnwindData |  |
| 15 | `EvtGetObjectArrayProperty` | `0x178E0` | 309 | UnwindData |  |
| 17 | `EvtGetPublisherMetadataProperty` | `0x18690` | 330 | UnwindData |  |
| 30 | `EvtNextEventMetadata` | `0x187E0` | 449 | UnwindData |  |
| 11 | `EvtGetEventInfo` | `0x18E00` | 217 | UnwindData |  |
| 6 | `EvtCreateBookmark` | `0x1DA20` | 179 | UnwindData |  |
| 19 | `EvtIntAssertConfig` | `0x1E890` | 361 | UnwindData |  |
| 12 | `EvtGetEventMetadataProperty` | `0x1EE20` | 319 | UnwindData |  |
| 36 | `EvtOpenPublisherEnum` | `0x1FA80` | 439 | UnwindData |  |
| 38 | `EvtOpenSession` | `0x1FDC0` | 449 | UnwindData |  |
| 34 | `EvtOpenEventMetadataEnum` | `0x1FFB0` | 314 | UnwindData |  |
| 18 | `EvtGetQueryInfo` | `0x211B0` | 952 | UnwindData |  |
| 2 | `EvtArchiveExportedLog` | `0x23710` | 502 | UnwindData |  |
| 3 | `EvtCancel` | `0x23910` | 157 | UnwindData |  |
| 4 | `EvtClearLog` | `0x239C0` | 394 | UnwindData |  |
| 13 | `EvtGetExtendedStatus` | `0x23B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EvtOpenChannelEnum` | `0x23B70` | 437 | UnwindData |  |
| 41 | `EvtSaveChannelConfig` | `0x23D30` | 222 | UnwindData |  |
| 43 | `EvtSetChannelConfigProperty` | `0x23E20` | 273 | UnwindData |  |
| 1 | `EvtIntSysprepCleanup` | `0x24080` | 151 | UnwindData |  |
| 20 | `EvtIntCreateBinXMLFromCustomXML` | `0x24250` | 65 | UnwindData |  |
| 21 | `EvtIntCreateLocalLogfile` | `0x242A0` | 257 | UnwindData |  |
| 22 | `EvtIntGetClassicLogDisplayName` | `0x243B0` | 963 | UnwindData |  |
| 23 | `EvtIntRenderResourceEventTemplate` | `0x24780` | 1,306 | UnwindData |  |
| 26 | `EvtIntRetractConfig` | `0x24CA0` | 343 | UnwindData |  |
| 27 | `EvtIntWriteXmlEventToLocalLogfile` | `0x24E00` | 626 | UnwindData |  |
