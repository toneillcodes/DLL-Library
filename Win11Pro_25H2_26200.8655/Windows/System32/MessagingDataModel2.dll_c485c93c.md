# Binary Specification: MessagingDataModel2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MessagingDataModel2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c485c93ca57f2f2ccdfa44685d3aa6438e4f80ad5e4f7cf18620791799218839`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 46 | `Messaging_GetMessagePreview` | `0x78B0` | 12,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `Messaging_GetUnFormattedMessagePreview` | `0x78B0` | 12,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DllCanUnloadNow` | `0xA9B0` | 42 | UnwindData |  |
| 23 | `DllGetClassObject` | `0xA9E0` | 4,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `Messaging_IsContentSupported` | `0xBD40` | 93 | UnwindData |  |
| 59 | `Messaging_IsMediaType` | `0xBDB0` | 301 | UnwindData |  |
| 1 | `?CommitAllAttachments@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x249D0` | 236 | UnwindData |  |
| 2 | `?CommitDeferredContent@MessagingDeferredAttachment@@YAJPEAUIStream@@0@Z` | `0x24AD0` | 343 | UnwindData |  |
| 3 | `?DeleteMessageAndTempFiles@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x24C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?DeleteTempFiles@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x24C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `?GetData@MessagingDeferredAttachment@@YAJPEAUISmAttachment@@PEAPEAUIStream@@1@Z` | `0x24C50` | 353 | UnwindData |  |
| 7 | `?GetDeferredAttachmentFilePath@MessagingDeferredAttachment@@YAJPEAUISmMessage@@KPEAHPEAV?$basic_string@GU?$char_traits@G@utl@@V?$allocator@G@2@@utl@@@Z` | `0x24DC0` | 642 | UnwindData |  |
| 8 | `GetDirectionalMarkerForCurrentLocale` | `0x25E00` | 142 | UnwindData |  |
| 35 | `Messaging_FormatPhoneNumber` | `0x26500` | 162 | UnwindData |  |
| 36 | `Messaging_FormatRecipient` | `0x265B0` | 406 | UnwindData |  |
| 38 | `Messaging_FormatStringWithLeftToRightMarkers` | `0x26750` | 235 | UnwindData |  |
| 39 | `Messaging_FormatStringWithLeftToRightMarkersIfPhoneNumber` | `0x26850` | 125 | UnwindData |  |
| 40 | `Messaging_GetAddressType` | `0x268E0` | 134 | UnwindData |  |
| 45 | `Messaging_GetMessageAttachmentText` | `0x26970` | 64 | UnwindData |  |
| 48 | `Messaging_GetRecipientsPreviewWithBiDiMarkers` | `0x269C0` | 873 | UnwindData |  |
| 69 | `Messaging_ResolveRecipientEx` | `0x26D30` | 267 | UnwindData |  |
| 20 | `Messaging_SmEntryIdToUdmObjectId` | `0x27080` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MOCloudCorrelation_CreateInstance2` | `0x27420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MessagingAsyncDeletion_CreateInstance` | `0x27430` | 54 | UnwindData |  |
| 31 | `Messaging_ChatTransportIdToStoreId` | `0x27470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `Messaging_FormatRecipientFromAggregate` | `0x27490` | 54 | UnwindData |  |
| 49 | `Messaging_GetRecipientsString` | `0x274D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Messaging_GetSmsCharacterCount` | `0x274F0` | 86 | UnwindData |  |
| 52 | `Messaging_GetValidSimId` | `0x27550` | 86 | UnwindData |  |
| 56 | `Messaging_IsCustomAppProviderId` | `0x275B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `Messaging_IsDataRoamingRestrictionActive` | `0x275D0` | 102 | UnwindData |  |
| 58 | `Messaging_IsFilterProviderId` | `0x27640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `Messaging_IsMmsMessage` | `0x27660` | 81 | UnwindData |  |
| 62 | `Messaging_IsRcsMessage` | `0x276C0` | 81 | UnwindData |  |
| 63 | `Messaging_IsSIMMessage` | `0x27720` | 167 | UnwindData |  |
| 64 | `Messaging_IsThreadedByRemoteConversationId` | `0x277D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `Messaging_IsVoiceRoamingRestrictionActive` | `0x277E0` | 93 | UnwindData |  |
| 71 | `Messaging_ShowToastForRcsEndUserMessage` | `0x27850` | 137 | UnwindData |  |
| 77 | `UnInitMessagingObjectModelModule` | `0x278E0` | 118 | UnwindData |  |
| 24 | `GetHasInternationalCapability` | `0x27CC0` | 92 | UnwindData |  |
| 32 | `Messaging_CreateMessageInConversation` | `0x27D30` | 459 | UnwindData |  |
| 33 | `Messaging_CreateMessageInConversationWithRecipients` | `0x27F10` | 311 | UnwindData |  |
| 34 | `Messaging_CreateMessageInConversationWithRecipientsAndRemoteId` | `0x28050` | 315 | UnwindData |  |
| 54 | `Messaging_InitializeRcsSlotMessagingSettings` | `0x281A0` | 317 | UnwindData |  |
| 61 | `Messaging_IsRcsEnabled` | `0x282F0` | 292 | UnwindData |  |
| 66 | `Messaging_MarkMessageAsFailed` | `0x28420` | 359 | UnwindData |  |
| 25 | `MOCloudCorrelation_CreateInstance` | `0x2C010` | 147 | UnwindData |  |
| 41 | `Messaging_GetContentTypeFromFilePath` | `0x2CE00` | 423 | UnwindData |  |
| 42 | `Messaging_GetFileExtensionFromContentType` | `0x2CFB0` | 272 | UnwindData |  |
| 44 | `Messaging_GetMediaTypeFromMimeTag` | `0x2D0D0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Messaging_MessagingOMStartupShutdown` | `0x2DD80` | 84 | UnwindData |  |
| 68 | `Messaging_MessagingOMStartupStoreScan` | `0x2DDE0` | 249 | UnwindData |  |
| 5 | `GetActiveMmsProfile` | `0x52050` | 526 | UnwindData |  |
| 9 | `GetMaxAuthorizedSizeOfMMS` | `0x52270` | 167 | UnwindData |  |
| 18 | `Messaging_GetMediaTempFilePath` | `0x523B0` | 102 | UnwindData |  |
| 19 | `Messaging_IsUnderMediaTempFolder` | `0x52420` | 367 | UnwindData |  |
| 43 | `Messaging_GetMediaTempFolder` | `0x528B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MessagingRegistryGetDWORDFromPerSimMmsProfile` | `0x528C0` | 166 | UnwindData |  |
| 11 | `MessagingRegistryGetDWORDPerSim` | `0x52970` | 366 | UnwindData |  |
| 12 | `MessagingRegistryGetStringFromPerSimMmsProfile` | `0x52AF0` | 166 | UnwindData |  |
| 13 | `MessagingRegistryGetStringPerSim` | `0x52BA0` | 470 | UnwindData |  |
| 14 | `MessagingRegistrySetDWORDPerSim` | `0x52D80` | 244 | UnwindData |  |
| 15 | `MessagingRegistrySetDWORDToPerSimMmsProfile` | `0x52E80` | 166 | UnwindData |  |
| 16 | `MessagingRegistrySetStringPerSim` | `0x52F30` | 243 | UnwindData |  |
| 17 | `MessagingRegistrySetStringToPerSimMmsProfile` | `0x53030` | 166 | UnwindData |  |
| 21 | `CellMessagingHelper_CreateInstance` | `0x55DC0` | 121 | UnwindData |  |
| 28 | `MessagingMultiSimConverter_CreateInstanceWithPhoneOM` | `0x5C030` | 188 | UnwindData |  |
| 29 | `MessagingMultiSimConverter_CreateInstanceWithSimOM` | `0x5C100` | 134 | UnwindData |  |
| 30 | `MessagingMultiSimConverter_CreateSynchronousInstanceWithSimOM` | `0x5C190` | 132 | UnwindData |  |
| 47 | `Messaging_GetPlatformType` | `0x5C2B0` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `WwanConnectionConfiguration_CreateInstance` | `0x5CD80` | 46 | UnwindData |  |
| 73 | `Messaging_ShutdownNotification` | `0x711C0` | 68 | UnwindData |  |
| 76 | `Messaging_StartNotification` | `0x71210` | 113 | UnwindData |  |
| 70 | `Messaging_RetryDownloadCloudServiceMessage` | `0x75830` | 58 | UnwindData |  |
| 72 | `Messaging_ShutdownCloudServices` | `0x75870` | 61 | UnwindData |  |
| 75 | `Messaging_StartCloudServices` | `0x758C0` | 129 | UnwindData |  |
| 74 | `Messaging_StartCloudServiceSync` | `0x75A10` | 184 | UnwindData |  |
| 53 | `Messaging_HasEmbeddedModem` | `0xB5E80` | 50 | UnwindData |  |
