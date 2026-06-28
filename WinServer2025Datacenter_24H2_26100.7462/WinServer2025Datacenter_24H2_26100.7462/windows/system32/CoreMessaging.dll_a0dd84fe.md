# Binary Specification: CoreMessaging.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CoreMessaging.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a0dd84fe4d829bea5158e9b2370a61040535fc91e9881356e289d511dd556403`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CoreUICallSendVaList` | `0x4DE50` | 102 | UnwindData |  |
| 1 | `CoreUICallComputeMaximumMessageSize` | `0x4E110` | 493 | UnwindData |  |
| 7 | `CoreUICallSend` | `0x4E310` | 110 | UnwindData |  |
| 6 | `CoreUICallReceive` | `0x5EFA0` | 202 | UnwindData |  |
| 18 | `CreateDispatcherQueueController` | `0x684E0` | 306 | UnwindData |  |
| 23 | `GetDispatcherQueueForCurrentThread` | `0x68DE0` | 42 | UnwindData |  |
| 15 | `CoreUIOpenExisting` | `0x69160` | 64 | UnwindData |  |
| 27 | `MsgRelease` | `0x6EC60` | 114 | UnwindData |  |
| 26 | `MsgBufferShare` | `0x70250` | 133 | UnwindData |  |
| 28 | `MsgStringCreateShared` | `0x702E0` | 282 | UnwindData |  |
| 24 | `MsgBlobCreateShared` | `0x70400` | 214 | UnwindData |  |
| 20 | `DllCanUnloadNow` | `0x72CC0` | 32 | UnwindData |  |
| 21 | `DllGetActivationFactory` | `0x72CF0` | 45 | UnwindData |  |
| 25 | `MsgBlobCreateStack` | `0x74B30` | 10,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MsgStringCreateStack` | `0x77280` | 6,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CoreUICallCreateEndpointHostWithSendPriority` | `0x78A40` | 211 | UnwindData |  |
| 2 | `CoreUICallCreateConversationHost` | `0x78B20` | 218 | UnwindData |  |
| 13 | `CoreUICreateEx` | `0x7E4F0` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SvchostPushServiceGlobals` | `0x7EF90` | 5,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `CoreUICreate` | `0x80350` | 42,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CoreUICallCreateEndpointHost` | `0x8A8F0` | 56,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CoreUIConfigureTestHost` | `0x98720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CoreUIConfigureUserIntegration` | `0x98740` | 197 | UnwindData |  |
| 14 | `CoreUIInitializeTestService` | `0x98810` | 31 | UnwindData |  |
| 17 | `CoreUIUninitializeTestService` | `0x98840` | 17 | UnwindData |  |
| 12 | `CoreUICreateAnonymousStream` | `0x98C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CoreUIRouteToTestRegistrar` | `0x98C20` | 88 | UnwindData |  |
| 30 | `ServiceMain` | `0x98ED0` | 146 | UnwindData |  |
| 5 | `CoreUICallGetAddressOfParameterInBuffer` | `0xC7040` | 106 | UnwindData |  |
| 19 | `CreateDispatcherQueueForCurrentThread` | `0xC9740` | 66 | UnwindData |  |
| 22 | `DllGetClassObject` | `0xC9840` | 65 | UnwindData |  |
