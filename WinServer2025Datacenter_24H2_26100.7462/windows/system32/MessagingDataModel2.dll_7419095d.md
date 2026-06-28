# Binary Specification: MessagingDataModel2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MessagingDataModel2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7419095da529e559adc263412f66ead33d0542118f93a158c307250f2ffe7ea2`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 46 | `Messaging_GetMessagePreview` | `0x7800` | 12,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `Messaging_GetUnFormattedMessagePreview` | `0x7800` | 12,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DllCanUnloadNow` | `0xA8A0` | 42 | UnwindData |  |
| 23 | `DllGetClassObject` | `0xA8D0` | 4,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `Messaging_IsContentSupported` | `0xBC30` | 93 | UnwindData |  |
| 59 | `Messaging_IsMediaType` | `0xBCA0` | 301 | UnwindData |  |
| 1 | `?CommitAllAttachments@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x248C0` | 236 | UnwindData |  |
| 2 | `?CommitDeferredContent@MessagingDeferredAttachment@@YAJPEAUIStream@@0@Z` | `0x249C0` | 343 | UnwindData |  |
| 3 | `?DeleteMessageAndTempFiles@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x24B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?DeleteTempFiles@MessagingDeferredAttachment@@YAJPEAUISmMessage@@@Z` | `0x24B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `?GetData@MessagingDeferredAttachment@@YAJPEAUISmAttachment@@PEAPEAUIStream@@1@Z` | `0x24B40` | 353 | UnwindData |  |
| 7 | `?GetDeferredAttachmentFilePath@MessagingDeferredAttachment@@YAJPEAUISmMessage@@KPEAHPEAV?$basic_string@GU?$char_traits@G@utl@@V?$allocator@G@2@@utl@@@Z` | `0x24CB0` | 642 | UnwindData |  |
| 8 | `GetDirectionalMarkerForCurrentLocale` | `0x25CF0` | 142 | UnwindData |  |
| 35 | `Messaging_FormatPhoneNumber` | `0x263F0` | 162 | UnwindData |  |
| 36 | `Messaging_FormatRecipient` | `0x264A0` | 406 | UnwindData |  |
| 38 | `Messaging_FormatStringWithLeftToRightMarkers` | `0x26640` | 235 | UnwindData |  |
| 39 | `Messaging_FormatStringWithLeftToRightMarkersIfPhoneNumber` | `0x26740` | 125 | UnwindData |  |
| 40 | `Messaging_GetAddressType` | `0x267D0` | 134 | UnwindData |  |
| 45 | `Messaging_GetMessageAttachmentText` | `0x26860` | 64 | UnwindData |  |
| 48 | `Messaging_GetRecipientsPreviewWithBiDiMarkers` | `0x268B0` | 873 | UnwindData |  |
| 69 | `Messaging_ResolveRecipientEx` | `0x26C20` | 267 | UnwindData |  |
| 20 | `Messaging_SmEntryIdToUdmObjectId` | `0x26F70` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MOCloudCorrelation_CreateInstance2` | `0x27310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MessagingAsyncDeletion_CreateInstance` | `0x27320` | 54 | UnwindData |  |
| 31 | `Messaging_ChatTransportIdToStoreId` | `0x27360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `Messaging_FormatRecipientFromAggregate` | `0x27380` | 54 | UnwindData |  |
| 49 | `Messaging_GetRecipientsString` | `0x273C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Messaging_GetSmsCharacterCount` | `0x273E0` | 86 | UnwindData |  |
| 52 | `Messaging_GetValidSimId` | `0x27440` | 86 | UnwindData |  |
| 56 | `Messaging_IsCustomAppProviderId` | `0x274A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `Messaging_IsDataRoamingRestrictionActive` | `0x274C0` | 102 | UnwindData |  |
| 58 | `Messaging_IsFilterProviderId` | `0x27530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `Messaging_IsMmsMessage` | `0x27550` | 81 | UnwindData |  |
| 62 | `Messaging_IsRcsMessage` | `0x275B0` | 81 | UnwindData |  |
| 63 | `Messaging_IsSIMMessage` | `0x27610` | 167 | UnwindData |  |
| 64 | `Messaging_IsThreadedByRemoteConversationId` | `0x276C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `Messaging_IsVoiceRoamingRestrictionActive` | `0x276D0` | 93 | UnwindData |  |
| 71 | `Messaging_ShowToastForRcsEndUserMessage` | `0x27740` | 137 | UnwindData |  |
| 77 | `UnInitMessagingObjectModelModule` | `0x277D0` | 118 | UnwindData |  |
| 24 | `GetHasInternationalCapability` | `0x27BB0` | 92 | UnwindData |  |
| 32 | `Messaging_CreateMessageInConversation` | `0x27C20` | 459 | UnwindData |  |
| 33 | `Messaging_CreateMessageInConversationWithRecipients` | `0x27E00` | 311 | UnwindData |  |
| 34 | `Messaging_CreateMessageInConversationWithRecipientsAndRemoteId` | `0x27F40` | 315 | UnwindData |  |
| 54 | `Messaging_InitializeRcsSlotMessagingSettings` | `0x28090` | 317 | UnwindData |  |
| 61 | `Messaging_IsRcsEnabled` | `0x281E0` | 292 | UnwindData |  |
| 66 | `Messaging_MarkMessageAsFailed` | `0x28310` | 359 | UnwindData |  |
| 25 | `MOCloudCorrelation_CreateInstance` | `0x2BF00` | 147 | UnwindData |  |
| 41 | `Messaging_GetContentTypeFromFilePath` | `0x2CCF0` | 423 | UnwindData |  |
| 42 | `Messaging_GetFileExtensionFromContentType` | `0x2CEA0` | 272 | UnwindData |  |
| 44 | `Messaging_GetMediaTypeFromMimeTag` | `0x2CFC0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Messaging_MessagingOMStartupShutdown` | `0x2DC70` | 84 | UnwindData |  |
| 68 | `Messaging_MessagingOMStartupStoreScan` | `0x2DCD0` | 249 | UnwindData |  |
| 5 | `GetActiveMmsProfile` | `0x51E60` | 526 | UnwindData |  |
| 9 | `GetMaxAuthorizedSizeOfMMS` | `0x52080` | 167 | UnwindData |  |
| 18 | `Messaging_GetMediaTempFilePath` | `0x521C0` | 102 | UnwindData |  |
| 19 | `Messaging_IsUnderMediaTempFolder` | `0x52230` | 367 | UnwindData |  |
| 43 | `Messaging_GetMediaTempFolder` | `0x526C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MessagingRegistryGetDWORDFromPerSimMmsProfile` | `0x526D0` | 166 | UnwindData |  |
| 11 | `MessagingRegistryGetDWORDPerSim` | `0x52780` | 366 | UnwindData |  |
| 12 | `MessagingRegistryGetStringFromPerSimMmsProfile` | `0x52900` | 166 | UnwindData |  |
| 13 | `MessagingRegistryGetStringPerSim` | `0x529B0` | 470 | UnwindData |  |
| 14 | `MessagingRegistrySetDWORDPerSim` | `0x52B90` | 244 | UnwindData |  |
| 15 | `MessagingRegistrySetDWORDToPerSimMmsProfile` | `0x52C90` | 166 | UnwindData |  |
| 16 | `MessagingRegistrySetStringPerSim` | `0x52D40` | 243 | UnwindData |  |
| 17 | `MessagingRegistrySetStringToPerSimMmsProfile` | `0x52E40` | 166 | UnwindData |  |
| 21 | `CellMessagingHelper_CreateInstance` | `0x55BD0` | 121 | UnwindData |  |
| 28 | `MessagingMultiSimConverter_CreateInstanceWithPhoneOM` | `0x5BE40` | 188 | UnwindData |  |
| 29 | `MessagingMultiSimConverter_CreateInstanceWithSimOM` | `0x5BF10` | 134 | UnwindData |  |
| 30 | `MessagingMultiSimConverter_CreateSynchronousInstanceWithSimOM` | `0x5BFA0` | 132 | UnwindData |  |
| 47 | `Messaging_GetPlatformType` | `0x5C0C0` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `WwanConnectionConfiguration_CreateInstance` | `0x5CB90` | 46 | UnwindData |  |
| 73 | `Messaging_ShutdownNotification` | `0x70FD0` | 68 | UnwindData |  |
| 76 | `Messaging_StartNotification` | `0x71020` | 113 | UnwindData |  |
| 70 | `Messaging_RetryDownloadCloudServiceMessage` | `0x75640` | 58 | UnwindData |  |
| 72 | `Messaging_ShutdownCloudServices` | `0x75680` | 61 | UnwindData |  |
| 75 | `Messaging_StartCloudServices` | `0x756D0` | 129 | UnwindData |  |
| 74 | `Messaging_StartCloudServiceSync` | `0x75820` | 184 | UnwindData |  |
| 53 | `Messaging_HasEmbeddedModem` | `0xB3000` | 50 | UnwindData |  |
