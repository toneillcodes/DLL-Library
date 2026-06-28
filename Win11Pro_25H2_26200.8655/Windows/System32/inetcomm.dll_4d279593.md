# Binary Specification: inetcomm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\inetcomm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4d2795934a3a8b8248685c25f4a448a0aaf04d62318f83af67a0abe5bebb5c4a`
* **Total Exported Functions:** 116

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 56 | `MimeOleCreateMessage` | `0x59F0` | 143 | UnwindData |  |
| 86 | `MimeOleInetDateToFileTime` | `0xFD20` | 1,593 | UnwindData |  |
| 78 | `MimeOleGetFileExtension` | `0x165D0` | 109 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x19260` | 136 | UnwindData |  |
| 75 | `MimeOleGetContentTypeExt` | `0x1A020` | 358 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x1CD30` | 100 | UnwindData |  |
| 103 | `MimeOleSetCompatMode` | `0x216E0` | 7,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MimeOleCreateVirtualStream` | `0x23260` | 68 | UnwindData |  |
| 37 | `HrGetDisplayNameWithSizeForFile` | `0x23550` | 186 | UnwindData |  |
| 83 | `MimeOleGetPropW` | `0x25D70` | 82 | UnwindData |  |
| 702 | *Ordinal Only* | `0x27BD0` | 24 | UnwindData |  |
| 27 | `GetDllMajorVersion` | `0x27BF0` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateCommunityTransport` | `0x28290` | 88 | UnwindData |  |
| 4 | `CreateIMAPTransport` | `0x282F0` | 60 | UnwindData |  |
| 5 | `CreateIMAPTransport2` | `0x282F0` | 60 | UnwindData |  |
| 6 | `CreateNNTPTransport` | `0x28340` | 60 | UnwindData |  |
| 7 | `CreatePOP3Transport` | `0x28390` | 60 | UnwindData |  |
| 8 | `CreateRASTransport` | `0x283E0` | 88 | UnwindData |  |
| 9 | `CreateRangeList` | `0x28440` | 70 | UnwindData |  |
| 10 | `CreateSMTPTransport` | `0x28490` | 73 | UnwindData |  |
| 705 | *Ordinal Only* | `0x284E0` | 146 | UnwindData |  |
| 703 | *Ordinal Only* | `0x28580` | 116 | UnwindData |  |
| 707 | *Ordinal Only* | `0x28600` | 309 | UnwindData |  |
| 704 | *Ordinal Only* | `0x28740` | 131 | UnwindData |  |
| 708 | *Ordinal Only* | `0x287D0` | 309 | UnwindData |  |
| 706 | *Ordinal Only* | `0x28910` | 257 | UnwindData |  |
| 47 | `MimeGetAddressFormatW` | `0x291F0` | 343 | UnwindData |  |
| 50 | `MimeOleClearDirtyTree` | `0x29350` | 82 | UnwindData |  |
| 52 | `MimeOleCreateBody` | `0x29680` | 80 | UnwindData |  |
| 53 | `MimeOleCreateByteStream` | `0x296E0` | 84 | UnwindData |  |
| 54 | `MimeOleCreateHashTable` | `0x29740` | 163 | UnwindData |  |
| 55 | `MimeOleCreateHeaderTable` | `0x297F0` | 155 | UnwindData |  |
| 57 | `MimeOleCreateMessageParts` | `0x298A0` | 94 | UnwindData |  |
| 58 | `MimeOleCreatePropertySet` | `0x29910` | 141 | UnwindData |  |
| 59 | `MimeOleCreateSecurity` | `0x299B0` | 88 | UnwindData |  |
| 61 | `MimeOleDecodeHeader` | `0x29A10` | 46 | UnwindData |  |
| 62 | `MimeOleEncodeHeader` | `0x29A50` | 46 | UnwindData |  |
| 64 | `MimeOleFindCharset` | `0x29A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `MimeOleGenerateCID` | `0x29AC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `MimeOleGenerateFileName` | `0x29B00` | 416 | UnwindData |  |
| 67 | `MimeOleGenerateMID` | `0x29CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `MimeOleGetAllocator` | `0x29D00` | 84 | UnwindData |  |
| 69 | `MimeOleGetBodyPropA` | `0x29D60` | 92 | UnwindData |  |
| 70 | `MimeOleGetBodyPropW` | `0x29DD0` | 92 | UnwindData |  |
| 71 | `MimeOleGetCertsFromThumbprints` | `0x29E40` | 390 | UnwindData |  |
| 72 | `MimeOleGetCharsetInfo` | `0x29FD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `MimeOleGetCodePageCharset` | `0x2A000` | 41 | UnwindData |  |
| 74 | `MimeOleGetCodePageInfo` | `0x2A030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `MimeOleGetDefaultCharset` | `0x2A060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `MimeOleGetExtContentType` | `0x2A080` | 224 | UnwindData |  |
| 79 | `MimeOleGetFileInfo` | `0x2A2C0` | 856 | UnwindData |  |
| 80 | `MimeOleGetFileInfoW` | `0x2A620` | 660 | UnwindData |  |
| 81 | `MimeOleGetInternat` | `0x2A8C0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `MimeOleGetPropA` | `0x2AA20` | 82 | UnwindData |  |
| 84 | `MimeOleGetPropertySchema` | `0x2AA80` | 65 | UnwindData |  |
| 85 | `MimeOleGetRelatedSection` | `0x2AAD0` | 594 | UnwindData |  |
| 87 | `MimeOleObjectFromMoniker` | `0x2B0A0` | 66 | UnwindData |  |
| 88 | `MimeOleOpenFileStream` | `0x2B0F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `MimeOleParseMhtmlUrl` | `0x2B120` | 323 | UnwindData |  |
| 90 | `MimeOleParseRfc822Address` | `0x2B270` | 126 | UnwindData |  |
| 91 | `MimeOleParseRfc822AddressW` | `0x2B300` | 107 | UnwindData |  |
| 101 | `MimeOleSetBodyPropA` | `0x2B380` | 85 | UnwindData |  |
| 102 | `MimeOleSetBodyPropW` | `0x2B3E0` | 85 | UnwindData |  |
| 104 | `MimeOleSetDefaultCharset` | `0x2B440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `MimeOleSetPropA` | `0x2B460` | 69 | UnwindData |  |
| 106 | `MimeOleSetPropW` | `0x2B4B0` | 69 | UnwindData |  |
| 107 | `MimeOleStripHeaders` | `0x2C1C0` | 669 | UnwindData |  |
| 108 | `MimeOleUnEscapeStringInPlace` | `0x2C470` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `MimeOleUnEscapeStringInPlaceW` | `0x2C4E0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MimeOleAlgNameFromSMimeCap` | `0x2CB90` | 538 | UnwindData |  |
| 49 | `MimeOleAlgStrengthFromSMimeCap` | `0x2CDB0` | 930 | UnwindData |  |
| 92 | `MimeOleSMimeCapAddCert` | `0x2D160` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `MimeOleSMimeCapAddSMimeCap` | `0x2D1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `MimeOleSMimeCapGetEncAlg` | `0x2D1D0` | 34 | UnwindData |  |
| 95 | `MimeOleSMimeCapGetHashAlg` | `0x2D200` | 34 | UnwindData |  |
| 96 | `MimeOleSMimeCapInit` | `0x2D230` | 580 | UnwindData |  |
| 97 | `MimeOleSMimeCapRelease` | `0x2D480` | 34 | UnwindData |  |
| 98 | `MimeOleSMimeCapsFromDlg` | `0x2D4B0` | 982 | UnwindData |  |
| 99 | `MimeOleSMimeCapsFull` | `0x2D890` | 394 | UnwindData |  |
| 100 | `MimeOleSMimeCapsToDlg` | `0x2DA20` | 979 | UnwindData |  |
| 51 | `MimeOleConvertEnrichedToHTML` | `0x2E040` | 1,515 | UnwindData |  |
| 63 | `MimeOleFileTimeToInetDate` | `0x2E640` | 464 | UnwindData |  |
| 1 | *Ordinal Only* | `0x65080` | 290 | UnwindData |  |
| 2 | `RichMimeEdit_CreateInstance` | `0x66E10` | 60 | UnwindData |  |
| 42 | `MimeEditCreateMimeDocument` | `0x69020` | 269 | UnwindData |  |
| 43 | `MimeEditDocumentFromStream` | `0x69140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MimeEditGetBackgroundImageUrl` | `0x69160` | 111 | UnwindData |  |
| 45 | `MimeEditIsSafeToRun` | `0x691E0` | 88 | UnwindData |  |
| 46 | `MimeEditViewSource` | `0x69240` | 174,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `HrAthGetFileName` | `0x93DC0` | 286 | UnwindData |  |
| 29 | `HrAthGetFileNameW` | `0x93EF0` | 170 | UnwindData |  |
| 30 | `HrAttachDataFromBodyPart` | `0x93FA0` | 405 | UnwindData |  |
| 31 | `HrAttachDataFromFile` | `0x94140` | 201 | UnwindData |  |
| 32 | `HrCreateDisplayNameWithSizeForFile` | `0x94260` | 286 | UnwindData |  |
| 33 | `HrDoAttachmentVerb` | `0x94390` | 812 | UnwindData |  |
| 34 | `HrFreeAttachData` | `0x946D0` | 86 | UnwindData |  |
| 35 | `HrGetAttachIcon` | `0x94730` | 181 | UnwindData |  |
| 36 | `HrGetAttachIconByFile` | `0x947F0` | 264 | UnwindData |  |
| 38 | `HrGetLastOpenFileDirectory` | `0x94900` | 141 | UnwindData |  |
| 39 | `HrGetLastOpenFileDirectoryW` | `0x949A0` | 76 | UnwindData |  |
| 40 | `HrSaveAttachToFile` | `0x94A00` | 506 | UnwindData |  |
| 41 | `HrSaveAttachmentAs` | `0x94C00` | 746 | UnwindData |  |
| 13 | `EssContentHintDecodeEx` | `0x96CF0` | 81 | UnwindData |  |
| 14 | `EssContentHintEncodeEx` | `0x96DF0` | 257 | UnwindData |  |
| 15 | `EssKeyExchPreferenceDecodeEx` | `0x96F00` | 81 | UnwindData |  |
| 16 | `EssKeyExchPreferenceEncodeEx` | `0x97130` | 360 | UnwindData |  |
| 17 | `EssMLHistoryDecodeEx` | `0x972A0` | 81 | UnwindData |  |
| 18 | `EssMLHistoryEncodeEx` | `0x974D0` | 600 | UnwindData |  |
| 19 | `EssReceiptDecodeEx` | `0x97730` | 78 | UnwindData |  |
| 20 | `EssReceiptEncodeEx` | `0x97890` | 251 | UnwindData |  |
| 21 | `EssReceiptRequestDecodeEx` | `0x979A0` | 81 | UnwindData |  |
| 22 | `EssReceiptRequestEncodeEx` | `0x97BE0` | 452 | UnwindData |  |
| 23 | `EssSecurityLabelDecodeEx` | `0x97DB0` | 81 | UnwindData |  |
| 24 | `EssSecurityLabelEncodeEx` | `0x97FF0` | 466 | UnwindData |  |
| 25 | `EssSignCertificateDecodeEx` | `0x981D0` | 81 | UnwindData |  |
| 26 | `EssSignCertificateEncodeEx` | `0x98290` | 81 | UnwindData |  |
