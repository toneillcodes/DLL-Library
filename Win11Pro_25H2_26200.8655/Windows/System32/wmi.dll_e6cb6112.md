# Binary Specification: wmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e6cb6112bcfbb38c199e88810b2ec2e0af20c29c2e5aa78c90980e5a9db22004`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseTrace` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-consumer-l1-1-0.CloseTrace` |
| 2 | `ControlTraceA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-legacy-l1-1-0.ControlTraceA` |
| 3 | `ControlTraceW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-controller-l1-1-0.ControlTraceW` |
| 4 | `CreateTraceInstanceId` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwCreateTraceInstanceId` |
| 5 | `EnableTrace` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-legacy-l1-1-0.EnableTrace` |
| 6 | `GetTraceEnableFlags` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-classicprovider-l1-1-0.GetTraceEnableFlags` |
| 7 | `GetTraceEnableLevel` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-classicprovider-l1-1-0.GetTraceEnableLevel` |
| 8 | `GetTraceLoggerHandle` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-classicprovider-l1-1-0.GetTraceLoggerHandle` |
| 9 | `OpenTraceA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-legacy-l1-1-0.OpenTraceA` |
| 10 | `OpenTraceW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-consumer-l1-1-0.OpenTraceW` |
| 11 | `ProcessTrace` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-consumer-l1-1-0.ProcessTrace` |
| 12 | `QueryAllTracesA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-legacy-l1-1-0.QueryAllTracesA` |
| 13 | `QueryAllTracesW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-controller-l1-1-0.QueryAllTracesW` |
| 14 | `RegisterTraceGuidsA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-obsolete-l1-1-0.RegisterTraceGuidsA` |
| 15 | `RegisterTraceGuidsW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-classicprovider-l1-1-0.RegisterTraceGuidsW` |
| 16 | `RemoveTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-obsolete-l1-1-0.RemoveTraceCallback` |
| 17 | `SetTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-obsolete-l1-1-0.SetTraceCallback` |
| 18 | `StartTraceA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-legacy-l1-1-0.StartTraceA` |
| 19 | `StartTraceW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-controller-l1-1-0.StartTraceW` |
| 20 | `TraceEvent` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwLogTraceEvent` |
| 21 | `TraceEventInstance` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceEventInstance` |
| 22 | `UnregisterTraceGuids` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-classicprovider-l1-1-0.UnregisterTraceGuids` |
| 23 | `WmiCloseBlock` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiCloseBlock` |
| 24 | `WmiDevInstToInstanceNameA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiDevInstToInstanceNameA` |
| 25 | `WmiDevInstToInstanceNameW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiDevInstToInstanceNameW` |
| 26 | `WmiEnumerateGuids` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiEnumerateGuids` |
| 27 | `WmiExecuteMethodA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiExecuteMethodA` |
| 28 | `WmiExecuteMethodW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiExecuteMethodW` |
| 29 | `WmiFileHandleToInstanceNameA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiFileHandleToInstanceNameA` |
| 30 | `WmiFileHandleToInstanceNameW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiFileHandleToInstanceNameW` |
| 31 | `WmiFreeBuffer` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiFreeBuffer` |
| 32 | `WmiMofEnumerateResourcesA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiMofEnumerateResourcesA` |
| 33 | `WmiMofEnumerateResourcesW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiMofEnumerateResourcesW` |
| 34 | `WmiNotificationRegistrationA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiNotificationRegistrationA` |
| 35 | `WmiNotificationRegistrationW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiNotificationRegistrationW` |
| 36 | `WmiOpenBlock` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiOpenBlock` |
| 37 | `WmiQueryAllDataA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiQueryAllDataA` |
| 38 | `WmiQueryAllDataW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiQueryAllDataW` |
| 39 | `WmiQueryGuidInformation` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiQueryGuidInformation` |
| 40 | `WmiQuerySingleInstanceA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiQuerySingleInstanceA` |
| 41 | `WmiQuerySingleInstanceW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiQuerySingleInstanceW` |
| 42 | `WmiSetSingleInstanceA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiSetSingleInstanceA` |
| 43 | `WmiSetSingleInstanceW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiSetSingleInstanceW` |
| 44 | `WmiSetSingleItemA` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiSetSingleItemA` |
| 45 | `WmiSetSingleItemW` | `0x0` | - | Forwarded | Forwarded to: `wmiclnt.WmiSetSingleItemW` |
