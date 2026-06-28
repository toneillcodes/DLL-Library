# Binary Specification: rpchttp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rpchttp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b2a8889142f43bd115ad44e70caef3ca3c41cf945c9d3b41ee167f9528cba265`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `I_RpcExtInitializeExtensionPoint` | `0x1010` | 2,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CompareHttpTransportCredentials` | `0x1930` | 301 | UnwindData |  |
| 2 | `ConvertToUnicodeHttpTransportCredentials` | `0x1A70` | 563 | UnwindData |  |
| 3 | `DuplicateHttpTransportCredentials` | `0x1CB0` | 428 | UnwindData |  |
| 4 | `FreeHttpTransportCredentials` | `0x1E70` | 171 | UnwindData |  |
| 13 | `I_RpcTransFreeHttpCredentials` | `0x1F30` | 67 | UnwindData |  |
| 14 | `I_RpcTransGetHttpCredentials` | `0x1F80` | 159 | UnwindData |  |
| 5 | `HTTP2GetRpcConnectionTransport` | `0xBE00` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `HTTP2ProcessComplexTReceive` | `0xC020` | 520 | UnwindData |  |
| 7 | `HTTP2ProcessComplexTSend` | `0xC230` | 158 | UnwindData |  |
| 8 | `HTTP2ProcessRuntimePostedEvent` | `0xC2E0` | 15 | UnwindData |  |
| 9 | `HTTP2TestHook` | `0xC490` | 165 | UnwindData |  |
| 11 | `HttpSendIdentifyResponse` | `0xDB10` | 51 | UnwindData |  |
| 15 | `WS_HTTP2_CONNECTION__Initialize` | `0x1C950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WS_HTTP2_INITIAL_CONNECTION__new` | `0x1C960` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `I_RpcProxyNewConnection` | `0x1CFE0` | 968 | UnwindData |  |
| 19 | `I_RpcReplyToClientWithStatus` | `0x1D3B0` | 4,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HttpParseNetworkOptions` | `0x1E520` | 1,944 | UnwindData |  |
| 12 | `I_RpcGetRpcProxy` | `0x1EF70` | 362 | UnwindData |  |
