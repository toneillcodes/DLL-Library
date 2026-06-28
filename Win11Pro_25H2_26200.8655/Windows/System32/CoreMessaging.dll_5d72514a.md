# Binary Specification: CoreMessaging.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CoreMessaging.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5d72514abe7f309088a6c4a0a1dbda87925ae2bbe74c1dd4c35b03a94f25e35e`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CoreUICallSendVaList` | `0x4DE00` | 102 | UnwindData |  |
| 1 | `CoreUICallComputeMaximumMessageSize` | `0x4E0C0` | 493 | UnwindData |  |
| 7 | `CoreUICallSend` | `0x4E2C0` | 110 | UnwindData |  |
| 6 | `CoreUICallReceive` | `0x5EF50` | 202 | UnwindData |  |
| 18 | `CreateDispatcherQueueController` | `0x68050` | 306 | UnwindData |  |
| 23 | `GetDispatcherQueueForCurrentThread` | `0x68950` | 42 | UnwindData |  |
| 15 | `CoreUIOpenExisting` | `0x68CD0` | 64 | UnwindData |  |
| 27 | `MsgRelease` | `0x6EBD0` | 114 | UnwindData |  |
| 26 | `MsgBufferShare` | `0x701C0` | 133 | UnwindData |  |
| 28 | `MsgStringCreateShared` | `0x70250` | 282 | UnwindData |  |
| 24 | `MsgBlobCreateShared` | `0x70370` | 214 | UnwindData |  |
| 20 | `DllCanUnloadNow` | `0x72C30` | 32 | UnwindData |  |
| 21 | `DllGetActivationFactory` | `0x72C60` | 45 | UnwindData |  |
| 25 | `MsgBlobCreateStack` | `0x74AA0` | 10,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MsgStringCreateStack` | `0x771F0` | 6,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CoreUICallCreateEndpointHostWithSendPriority` | `0x789B0` | 211 | UnwindData |  |
| 2 | `CoreUICallCreateConversationHost` | `0x78A90` | 218 | UnwindData |  |
| 13 | `CoreUICreateEx` | `0x7E460` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SvchostPushServiceGlobals` | `0x7EF00` | 5,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `CoreUICreate` | `0x802C0` | 42,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CoreUICallCreateEndpointHost` | `0x8A860` | 56,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CoreUIConfigureTestHost` | `0x98520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CoreUIConfigureUserIntegration` | `0x98540` | 197 | UnwindData |  |
| 14 | `CoreUIInitializeTestService` | `0x98610` | 31 | UnwindData |  |
| 17 | `CoreUIUninitializeTestService` | `0x98640` | 17 | UnwindData |  |
| 12 | `CoreUICreateAnonymousStream` | `0x98A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CoreUIRouteToTestRegistrar` | `0x98A20` | 88 | UnwindData |  |
| 30 | `ServiceMain` | `0x98CD0` | 146 | UnwindData |  |
| 5 | `CoreUICallGetAddressOfParameterInBuffer` | `0xC5470` | 106 | UnwindData |  |
| 19 | `CreateDispatcherQueueForCurrentThread` | `0xC7BA0` | 66 | UnwindData |  |
| 22 | `DllGetClassObject` | `0xC7CA0` | 65 | UnwindData |  |
