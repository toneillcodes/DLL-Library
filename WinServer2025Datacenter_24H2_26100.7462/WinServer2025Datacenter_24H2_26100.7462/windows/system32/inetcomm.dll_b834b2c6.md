# Binary Specification: inetcomm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\inetcomm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b834b2c6f4e570a862e9611d5a16e58bd75690d0aec422ac066b311e329b529a`
* **Total Exported Functions:** 116

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 56 | `MimeOleCreateMessage` | `0x59E0` | 143 | UnwindData |  |
| 86 | `MimeOleInetDateToFileTime` | `0xFD10` | 1,593 | UnwindData |  |
| 78 | `MimeOleGetFileExtension` | `0x165C0` | 109 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x19250` | 136 | UnwindData |  |
| 75 | `MimeOleGetContentTypeExt` | `0x1A010` | 358 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x1CD20` | 100 | UnwindData |  |
| 103 | `MimeOleSetCompatMode` | `0x216D0` | 7,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MimeOleCreateVirtualStream` | `0x23250` | 68 | UnwindData |  |
| 37 | `HrGetDisplayNameWithSizeForFile` | `0x23540` | 186 | UnwindData |  |
| 83 | `MimeOleGetPropW` | `0x25D60` | 82 | UnwindData |  |
| 702 | *Ordinal Only* | `0x27BC0` | 24 | UnwindData |  |
| 27 | `GetDllMajorVersion` | `0x27BE0` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateCommunityTransport` | `0x28280` | 88 | UnwindData |  |
| 4 | `CreateIMAPTransport` | `0x282E0` | 60 | UnwindData |  |
| 5 | `CreateIMAPTransport2` | `0x282E0` | 60 | UnwindData |  |
| 6 | `CreateNNTPTransport` | `0x28330` | 60 | UnwindData |  |
| 7 | `CreatePOP3Transport` | `0x28380` | 60 | UnwindData |  |
| 8 | `CreateRASTransport` | `0x283D0` | 88 | UnwindData |  |
| 9 | `CreateRangeList` | `0x28430` | 70 | UnwindData |  |
| 10 | `CreateSMTPTransport` | `0x28480` | 73 | UnwindData |  |
| 705 | *Ordinal Only* | `0x284D0` | 146 | UnwindData |  |
| 703 | *Ordinal Only* | `0x28570` | 116 | UnwindData |  |
| 707 | *Ordinal Only* | `0x285F0` | 309 | UnwindData |  |
| 704 | *Ordinal Only* | `0x28730` | 131 | UnwindData |  |
| 708 | *Ordinal Only* | `0x287C0` | 309 | UnwindData |  |
| 706 | *Ordinal Only* | `0x28900` | 257 | UnwindData |  |
| 47 | `MimeGetAddressFormatW` | `0x291E0` | 343 | UnwindData |  |
| 50 | `MimeOleClearDirtyTree` | `0x29340` | 82 | UnwindData |  |
| 52 | `MimeOleCreateBody` | `0x29670` | 80 | UnwindData |  |
| 53 | `MimeOleCreateByteStream` | `0x296D0` | 84 | UnwindData |  |
| 54 | `MimeOleCreateHashTable` | `0x29730` | 163 | UnwindData |  |
| 55 | `MimeOleCreateHeaderTable` | `0x297E0` | 155 | UnwindData |  |
| 57 | `MimeOleCreateMessageParts` | `0x29890` | 94 | UnwindData |  |
| 58 | `MimeOleCreatePropertySet` | `0x29900` | 141 | UnwindData |  |
| 59 | `MimeOleCreateSecurity` | `0x299A0` | 88 | UnwindData |  |
| 61 | `MimeOleDecodeHeader` | `0x29A00` | 46 | UnwindData |  |
| 62 | `MimeOleEncodeHeader` | `0x29A40` | 46 | UnwindData |  |
| 64 | `MimeOleFindCharset` | `0x29A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `MimeOleGenerateCID` | `0x29AB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `MimeOleGenerateFileName` | `0x29AF0` | 416 | UnwindData |  |
| 67 | `MimeOleGenerateMID` | `0x29CA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `MimeOleGetAllocator` | `0x29CF0` | 84 | UnwindData |  |
| 69 | `MimeOleGetBodyPropA` | `0x29D50` | 92 | UnwindData |  |
| 70 | `MimeOleGetBodyPropW` | `0x29DC0` | 92 | UnwindData |  |
| 71 | `MimeOleGetCertsFromThumbprints` | `0x29E30` | 390 | UnwindData |  |
| 72 | `MimeOleGetCharsetInfo` | `0x29FC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `MimeOleGetCodePageCharset` | `0x29FF0` | 41 | UnwindData |  |
| 74 | `MimeOleGetCodePageInfo` | `0x2A020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `MimeOleGetDefaultCharset` | `0x2A050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `MimeOleGetExtContentType` | `0x2A070` | 224 | UnwindData |  |
| 79 | `MimeOleGetFileInfo` | `0x2A2B0` | 856 | UnwindData |  |
| 80 | `MimeOleGetFileInfoW` | `0x2A610` | 660 | UnwindData |  |
| 81 | `MimeOleGetInternat` | `0x2A8B0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `MimeOleGetPropA` | `0x2AA10` | 82 | UnwindData |  |
| 84 | `MimeOleGetPropertySchema` | `0x2AA70` | 65 | UnwindData |  |
| 85 | `MimeOleGetRelatedSection` | `0x2AAC0` | 594 | UnwindData |  |
| 87 | `MimeOleObjectFromMoniker` | `0x2B090` | 66 | UnwindData |  |
| 88 | `MimeOleOpenFileStream` | `0x2B0E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `MimeOleParseMhtmlUrl` | `0x2B110` | 323 | UnwindData |  |
| 90 | `MimeOleParseRfc822Address` | `0x2B260` | 126 | UnwindData |  |
| 91 | `MimeOleParseRfc822AddressW` | `0x2B2F0` | 107 | UnwindData |  |
| 101 | `MimeOleSetBodyPropA` | `0x2B370` | 85 | UnwindData |  |
| 102 | `MimeOleSetBodyPropW` | `0x2B3D0` | 85 | UnwindData |  |
| 104 | `MimeOleSetDefaultCharset` | `0x2B430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `MimeOleSetPropA` | `0x2B450` | 69 | UnwindData |  |
| 106 | `MimeOleSetPropW` | `0x2B4A0` | 69 | UnwindData |  |
| 107 | `MimeOleStripHeaders` | `0x2C1B0` | 669 | UnwindData |  |
| 108 | `MimeOleUnEscapeStringInPlace` | `0x2C460` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `MimeOleUnEscapeStringInPlaceW` | `0x2C4D0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MimeOleAlgNameFromSMimeCap` | `0x2CB80` | 538 | UnwindData |  |
| 49 | `MimeOleAlgStrengthFromSMimeCap` | `0x2CDA0` | 930 | UnwindData |  |
| 92 | `MimeOleSMimeCapAddCert` | `0x2D150` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `MimeOleSMimeCapAddSMimeCap` | `0x2D1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `MimeOleSMimeCapGetEncAlg` | `0x2D1C0` | 34 | UnwindData |  |
| 95 | `MimeOleSMimeCapGetHashAlg` | `0x2D1F0` | 34 | UnwindData |  |
| 96 | `MimeOleSMimeCapInit` | `0x2D220` | 580 | UnwindData |  |
| 97 | `MimeOleSMimeCapRelease` | `0x2D470` | 34 | UnwindData |  |
| 98 | `MimeOleSMimeCapsFromDlg` | `0x2D4A0` | 982 | UnwindData |  |
| 99 | `MimeOleSMimeCapsFull` | `0x2D880` | 394 | UnwindData |  |
| 100 | `MimeOleSMimeCapsToDlg` | `0x2DA10` | 979 | UnwindData |  |
| 51 | `MimeOleConvertEnrichedToHTML` | `0x2E030` | 1,515 | UnwindData |  |
| 63 | `MimeOleFileTimeToInetDate` | `0x2E630` | 464 | UnwindData |  |
| 1 | *Ordinal Only* | `0x64F50` | 290 | UnwindData |  |
| 2 | `RichMimeEdit_CreateInstance` | `0x66CE0` | 60 | UnwindData |  |
| 42 | `MimeEditCreateMimeDocument` | `0x68EF0` | 269 | UnwindData |  |
| 43 | `MimeEditDocumentFromStream` | `0x69010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MimeEditGetBackgroundImageUrl` | `0x69030` | 111 | UnwindData |  |
| 45 | `MimeEditIsSafeToRun` | `0x690B0` | 88 | UnwindData |  |
| 46 | `MimeEditViewSource` | `0x69110` | 174,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `HrAthGetFileName` | `0x93C60` | 286 | UnwindData |  |
| 29 | `HrAthGetFileNameW` | `0x93D90` | 170 | UnwindData |  |
| 30 | `HrAttachDataFromBodyPart` | `0x93E40` | 405 | UnwindData |  |
| 31 | `HrAttachDataFromFile` | `0x93FE0` | 201 | UnwindData |  |
| 32 | `HrCreateDisplayNameWithSizeForFile` | `0x94100` | 286 | UnwindData |  |
| 33 | `HrDoAttachmentVerb` | `0x94230` | 812 | UnwindData |  |
| 34 | `HrFreeAttachData` | `0x94570` | 86 | UnwindData |  |
| 35 | `HrGetAttachIcon` | `0x945D0` | 181 | UnwindData |  |
| 36 | `HrGetAttachIconByFile` | `0x94690` | 264 | UnwindData |  |
| 38 | `HrGetLastOpenFileDirectory` | `0x947A0` | 141 | UnwindData |  |
| 39 | `HrGetLastOpenFileDirectoryW` | `0x94840` | 76 | UnwindData |  |
| 40 | `HrSaveAttachToFile` | `0x948A0` | 506 | UnwindData |  |
| 41 | `HrSaveAttachmentAs` | `0x94AA0` | 746 | UnwindData |  |
| 13 | `EssContentHintDecodeEx` | `0x96B90` | 81 | UnwindData |  |
| 14 | `EssContentHintEncodeEx` | `0x96C90` | 257 | UnwindData |  |
| 15 | `EssKeyExchPreferenceDecodeEx` | `0x96DA0` | 81 | UnwindData |  |
| 16 | `EssKeyExchPreferenceEncodeEx` | `0x96FD0` | 360 | UnwindData |  |
| 17 | `EssMLHistoryDecodeEx` | `0x97140` | 81 | UnwindData |  |
| 18 | `EssMLHistoryEncodeEx` | `0x97370` | 600 | UnwindData |  |
| 19 | `EssReceiptDecodeEx` | `0x975D0` | 78 | UnwindData |  |
| 20 | `EssReceiptEncodeEx` | `0x97730` | 251 | UnwindData |  |
| 21 | `EssReceiptRequestDecodeEx` | `0x97840` | 81 | UnwindData |  |
| 22 | `EssReceiptRequestEncodeEx` | `0x97A80` | 452 | UnwindData |  |
| 23 | `EssSecurityLabelDecodeEx` | `0x97C50` | 81 | UnwindData |  |
| 24 | `EssSecurityLabelEncodeEx` | `0x97E90` | 466 | UnwindData |  |
| 25 | `EssSignCertificateDecodeEx` | `0x98070` | 81 | UnwindData |  |
| 26 | `EssSignCertificateEncodeEx` | `0x98130` | 81 | UnwindData |  |
