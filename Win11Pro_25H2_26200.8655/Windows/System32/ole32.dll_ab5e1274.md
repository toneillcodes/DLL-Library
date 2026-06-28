# Binary Specification: ole32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ole32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab5e1274aeafb670e63b27b3f60dad8f2aafb95f26158d9e2893750e3aeafc0f`
* **Total Exported Functions:** 557

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 837 | `CLIPFORMAT_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserFree` |
| 838 | `CLIPFORMAT_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserFree64` |
| 839 | `CLIPFORMAT_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserMarshal` |
| 840 | `CLIPFORMAT_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserMarshal64` |
| 841 | `CLIPFORMAT_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserSize` |
| 842 | `CLIPFORMAT_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserSize64` |
| 843 | `CLIPFORMAT_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserUnmarshal` |
| 844 | `CLIPFORMAT_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.CLIPFORMAT_UserUnmarshal64` |
| 845 | `CLSIDFromOle1Class` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CLSIDFromOle1Class` |
| 846 | `CLSIDFromProgID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CLSIDFromProgID` |
| 847 | `CLSIDFromProgIDEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-2.CLSIDFromProgIDEx` |
| 848 | `CLSIDFromString` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CLSIDFromString` |
| 849 | `CStdAsyncStubBuffer2_Connect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer2_Connect` |
| 850 | `CStdAsyncStubBuffer2_Disconnect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer2_Disconnect` |
| 851 | `CStdAsyncStubBuffer2_Release` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer2_Release` |
| 852 | `CStdAsyncStubBuffer_AddRef` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_AddRef` |
| 853 | `CStdAsyncStubBuffer_Connect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_Connect` |
| 854 | `CStdAsyncStubBuffer_Disconnect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_Disconnect` |
| 855 | `CStdAsyncStubBuffer_Invoke` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_Invoke` |
| 856 | `CStdAsyncStubBuffer_QueryInterface` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_QueryInterface` |
| 857 | `CStdAsyncStubBuffer_Release` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdAsyncStubBuffer_Release` |
| 858 | `CStdStubBuffer2_Connect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdStubBuffer2_Connect` |
| 859 | `CStdStubBuffer2_CountRefs` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdStubBuffer2_CountRefs` |
| 860 | `CStdStubBuffer2_Disconnect` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdStubBuffer2_Disconnect` |
| 861 | `CStdStubBuffer2_QueryInterface` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.CStdStubBuffer2_QueryInterface` |
| 864 | `CoAddRefServerProcess` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoAddRefServerProcess` |
| 867 | `CoAllowUnmarshalerCLSID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoAllowUnmarshalerCLSID` |
| 869 | `CoCancelCall` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCancelCall` |
| 871 | `CoCopyProxy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCopyProxy` |
| 872 | `CoCreateFreeThreadedMarshaler` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCreateFreeThreadedMarshaler` |
| 873 | `CoCreateGuid` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCreateGuid` |
| 874 | `CoCreateInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCreateInstance` |
| 875 | `CoCreateInstanceEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCreateInstanceEx` |
| 876 | `CoCreateInstanceFromApp` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoCreateInstanceFromApp` |
| 877 | `CoCreateObjectInContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoCreateObjectInContext` |
| 878 | `CoDeactivateObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoDeactivateObject` |
| 879 | `CoDecodeProxy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoDecodeProxy` |
| 880 | `CoDecrementMTAUsage` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoDecrementMTAUsage` |
| 881 | `CoDisableCallCancellation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoDisableCallCancellation` |
| 882 | `CoDisconnectContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoDisconnectContext` |
| 883 | `CoDisconnectObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoDisconnectObject` |
| 885 | `CoEnableCallCancellation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoEnableCallCancellation` |
| 886 | `CoFileTimeNow` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-2.CoFileTimeNow` |
| 890 | `CoFreeUnusedLibraries` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoFreeUnusedLibraries` |
| 891 | `CoFreeUnusedLibrariesEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoFreeUnusedLibrariesEx` |
| 892 | `CoGetActivationState` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetActivationState` |
| 893 | `CoGetApartmentID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetApartmentID` |
| 894 | `CoGetApartmentType` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetApartmentType` |
| 895 | `CoGetCallContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetCallContext` |
| 896 | `CoGetCallState` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetCallState` |
| 897 | `CoGetCallerTID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetCallerTID` |
| 898 | `CoGetCancelObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetCancelObject` |
| 899 | `CoGetClassObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetClassObject` |
| 900 | `CoGetClassVersion` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetClassVersion` |
| 901 | `CoGetComCatalog` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.GetCatalogHelper` |
| 902 | `CoGetContextToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetContextToken` |
| 903 | `CoGetCurrentLogicalThreadId` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetCurrentLogicalThreadId` |
| 904 | `CoGetCurrentProcess` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetCurrentProcess` |
| 905 | `CoGetDefaultContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetDefaultContext` |
| 906 | `CoGetInstanceFromFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetInstanceFromFile` |
| 907 | `CoGetInstanceFromIStorage` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetInstanceFromIStorage` |
| 911 | `CoGetInterfaceAndReleaseStream` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetInterfaceAndReleaseStream` |
| 912 | `CoGetMalloc` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetMalloc` |
| 913 | `CoGetMarshalSizeMax` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetMarshalSizeMax` |
| 914 | `CoGetModuleType` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetModuleType` |
| 916 | `CoGetObjectContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetObjectContext` |
| 917 | `CoGetPSClsid` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetPSClsid` |
| 918 | `CoGetProcessIdentifier` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetProcessIdentifier` |
| 919 | `CoGetStandardMarshal` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetStandardMarshal` |
| 920 | `CoGetStdMarshalEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetStdMarshalEx` |
| 921 | `CoGetSystemSecurityPermissions` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetSystemSecurityPermissions` |
| 923 | `CoGetTreatAsClass` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoGetTreatAsClass` |
| 924 | `CoHandlePriorityEventsFromMessagePump` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.#111` |
| 925 | `CoImpersonateClient` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoImpersonateClient` |
| 926 | `CoIncrementMTAUsage` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoIncrementMTAUsage` |
| 928 | `CoInitializeEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoInitializeEx` |
| 929 | `CoInitializeSecurity` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoInitializeSecurity` |
| 932 | `CoInvalidateRemoteMachineBindings` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoInvalidateRemoteMachineBindings` |
| 933 | `CoIsHandlerConnected` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoIsHandlerConnected` |
| 934 | `CoIsOle1Class` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-3-1.CoIsOle1Class` |
| 936 | `CoLockObjectExternal` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoLockObjectExternal` |
| 937 | `CoMarshalHresult` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoMarshalHresult` |
| 938 | `CoMarshalInterThreadInterfaceInStream` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoMarshalInterThreadInterfaceInStream` |
| 939 | `CoMarshalInterface` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoMarshalInterface` |
| 940 | `CoPopServiceDomain` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoPopServiceDomain` |
| 941 | `CoPushServiceDomain` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoPushServiceDomain` |
| 942 | `CoQueryAuthenticationServices` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoQueryAuthenticationServices` |
| 943 | `CoQueryClientBlanket` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoQueryClientBlanket` |
| 944 | `CoQueryProxyBlanket` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoQueryProxyBlanket` |
| 946 | `CoReactivateObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoReactivateObject` |
| 947 | `CoRegisterActivationFilter` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRegisterActivationFilter` |
| 948 | `CoRegisterChannelHook` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.#112` |
| 949 | `CoRegisterClassObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRegisterClassObject` |
| 950 | `CoRegisterInitializeSpy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoRegisterInitializeSpy` |
| 951 | `CoRegisterMallocSpy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoRegisterMallocSpy` |
| 953 | `CoRegisterPSClsid` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRegisterPSClsid` |
| 954 | `CoRegisterSurrogate` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRegisterSurrogate` |
| 956 | `CoReleaseMarshalData` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoReleaseMarshalData` |
| 957 | `CoReleaseServerProcess` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoReleaseServerProcess` |
| 958 | `CoResumeClassObjects` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoResumeClassObjects` |
| 959 | `CoRetireServer` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoRetireServer` |
| 960 | `CoRevertToSelf` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRevertToSelf` |
| 961 | `CoRevokeClassObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoRevokeClassObject` |
| 962 | `CoRevokeInitializeSpy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoRevokeInitializeSpy` |
| 963 | `CoRevokeMallocSpy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoRevokeMallocSpy` |
| 964 | `CoSetCancelObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoSetCancelObject` |
| 965 | `CoSetMessageDispatcher` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.#110` |
| 966 | `CoSetProxyBlanket` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoSetProxyBlanket` |
| 968 | `CoSuspendClassObjects` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoSuspendClassObjects` |
| 969 | `CoSwitchCallContext` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoSwitchCallContext` |
| 970 | `CoTaskMemAlloc` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoTaskMemAlloc` |
| 971 | `CoTaskMemFree` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoTaskMemFree` |
| 972 | `CoTaskMemRealloc` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoTaskMemRealloc` |
| 973 | `CoTestCancel` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoTestCancel` |
| 974 | `CoTreatAsClass` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-3-1.CoTreatAsClass` |
| 976 | `CoUninitialize` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoUninitialize` |
| 978 | `CoUnmarshalHresult` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoUnmarshalHresult` |
| 979 | `CoUnmarshalInterface` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoUnmarshalInterface` |
| 980 | `CoVrfCheckThreadState` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoVrfCheckThreadState` |
| 981 | `CoVrfGetThreadState` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoVrfGetThreadState` |
| 982 | `CoVrfReleaseThreadState` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoVrfReleaseThreadState` |
| 983 | `CoWaitForMultipleHandles` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoWaitForMultipleHandles` |
| 984 | `CoWaitForMultipleObjects` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CoWaitForMultipleObjects` |
| 994 | `CreateErrorInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoCreateErrorInfo` |
| 1003 | `CreateStreamOnHGlobal` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.CreateStreamOnHGlobal` |
| 1004 | `DcomChannelSetHResult` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.DcomChannelSetHResult` |
| 1008 | `DllDebugObjectRPCHook` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.DllDebugObjectRPCHook` |
| 1014 | `EnableHookObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.EnableHookObject` |
| 1017 | `FreePropVariantArray` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.FreePropVariantArray` |
| 1022 | `GetErrorInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoGetErrorInfo` |
| 1024 | `GetHGlobalFromStream` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.GetHGlobalFromStream` |
| 1025 | `GetHookInterface` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.GetHookInterface` |
| 1028 | `HACCEL_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserFree` |
| 1029 | `HACCEL_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserFree64` |
| 1030 | `HACCEL_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserMarshal` |
| 1031 | `HACCEL_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserMarshal64` |
| 1032 | `HACCEL_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserSize` |
| 1033 | `HACCEL_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserSize64` |
| 1034 | `HACCEL_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserUnmarshal` |
| 1035 | `HACCEL_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HACCEL_UserUnmarshal64` |
| 1036 | `HBITMAP_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserFree` |
| 1037 | `HBITMAP_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserFree64` |
| 1038 | `HBITMAP_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserMarshal` |
| 1039 | `HBITMAP_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserMarshal64` |
| 1040 | `HBITMAP_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserSize` |
| 1041 | `HBITMAP_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserSize64` |
| 1042 | `HBITMAP_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserUnmarshal` |
| 1043 | `HBITMAP_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBITMAP_UserUnmarshal64` |
| 1044 | `HBRUSH_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserFree` |
| 1045 | `HBRUSH_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserFree64` |
| 1046 | `HBRUSH_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserMarshal` |
| 1047 | `HBRUSH_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserMarshal64` |
| 1048 | `HBRUSH_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserSize` |
| 1049 | `HBRUSH_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserSize64` |
| 1050 | `HBRUSH_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserUnmarshal` |
| 1051 | `HBRUSH_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HBRUSH_UserUnmarshal64` |
| 1052 | `HDC_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserFree` |
| 1053 | `HDC_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserFree64` |
| 1054 | `HDC_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserMarshal` |
| 1055 | `HDC_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserMarshal64` |
| 1056 | `HDC_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserSize` |
| 1057 | `HDC_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserSize64` |
| 1058 | `HDC_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserUnmarshal` |
| 1059 | `HDC_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HDC_UserUnmarshal64` |
| 1068 | `HGLOBAL_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserFree` |
| 1069 | `HGLOBAL_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserFree64` |
| 1070 | `HGLOBAL_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserMarshal` |
| 1071 | `HGLOBAL_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserMarshal64` |
| 1072 | `HGLOBAL_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserSize` |
| 1073 | `HGLOBAL_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserSize64` |
| 1074 | `HGLOBAL_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserUnmarshal` |
| 1075 | `HGLOBAL_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HGLOBAL_UserUnmarshal64` |
| 1076 | `HICON_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserFree` |
| 1077 | `HICON_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserFree64` |
| 1078 | `HICON_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserMarshal` |
| 1079 | `HICON_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserMarshal64` |
| 1080 | `HICON_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserSize` |
| 1081 | `HICON_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserSize64` |
| 1082 | `HICON_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserUnmarshal` |
| 1083 | `HICON_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HICON_UserUnmarshal64` |
| 1084 | `HMENU_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserFree` |
| 1085 | `HMENU_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserFree64` |
| 1086 | `HMENU_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserMarshal` |
| 1087 | `HMENU_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserMarshal64` |
| 1088 | `HMENU_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserSize` |
| 1089 | `HMENU_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserSize64` |
| 1090 | `HMENU_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserUnmarshal` |
| 1091 | `HMENU_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMENU_UserUnmarshal64` |
| 1108 | `HMONITOR_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserFree` |
| 1109 | `HMONITOR_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserFree64` |
| 1110 | `HMONITOR_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserMarshal` |
| 1111 | `HMONITOR_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserMarshal64` |
| 1112 | `HMONITOR_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserSize` |
| 1113 | `HMONITOR_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserSize64` |
| 1114 | `HMONITOR_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserUnmarshal` |
| 1115 | `HMONITOR_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HMONITOR_UserUnmarshal64` |
| 1116 | `HPALETTE_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserFree` |
| 1117 | `HPALETTE_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserFree64` |
| 1118 | `HPALETTE_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserMarshal` |
| 1119 | `HPALETTE_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserMarshal64` |
| 1120 | `HPALETTE_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserSize` |
| 1121 | `HPALETTE_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserSize64` |
| 1122 | `HPALETTE_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserUnmarshal` |
| 1123 | `HPALETTE_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HPALETTE_UserUnmarshal64` |
| 1124 | `HRGN_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HRGN_UserFree` |
| 1125 | `HRGN_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HRGN_UserMarshal` |
| 1126 | `HRGN_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HRGN_UserSize` |
| 1127 | `HRGN_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HRGN_UserUnmarshal` |
| 1128 | `HWND_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserFree` |
| 1129 | `HWND_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserFree64` |
| 1130 | `HWND_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserMarshal` |
| 1131 | `HWND_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserMarshal64` |
| 1132 | `HWND_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserSize` |
| 1133 | `HWND_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserSize64` |
| 1134 | `HWND_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserUnmarshal` |
| 1135 | `HWND_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserUnmarshal64` |
| 1136 | `HkOleRegisterObject` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.HkOleRegisterObject` |
| 1137 | `IIDFromString` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.IIDFromString` |
| 1148 | `NdrOleInitializeExtension` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.NdrOleInitializeExtension` |
| 1149 | `NdrProxyForwardingFunction10` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction10` |
| 1150 | `NdrProxyForwardingFunction11` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction11` |
| 1151 | `NdrProxyForwardingFunction12` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction12` |
| 1152 | `NdrProxyForwardingFunction13` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction13` |
| 1153 | `NdrProxyForwardingFunction14` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction14` |
| 1154 | `NdrProxyForwardingFunction15` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction15` |
| 1155 | `NdrProxyForwardingFunction16` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction16` |
| 1156 | `NdrProxyForwardingFunction17` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction17` |
| 1157 | `NdrProxyForwardingFunction18` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction18` |
| 1158 | `NdrProxyForwardingFunction19` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction19` |
| 1159 | `NdrProxyForwardingFunction20` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction20` |
| 1160 | `NdrProxyForwardingFunction21` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction21` |
| 1161 | `NdrProxyForwardingFunction22` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction22` |
| 1162 | `NdrProxyForwardingFunction23` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction23` |
| 1163 | `NdrProxyForwardingFunction24` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction24` |
| 1164 | `NdrProxyForwardingFunction25` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction25` |
| 1165 | `NdrProxyForwardingFunction26` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction26` |
| 1166 | `NdrProxyForwardingFunction27` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction27` |
| 1167 | `NdrProxyForwardingFunction28` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction28` |
| 1168 | `NdrProxyForwardingFunction29` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction29` |
| 1169 | `NdrProxyForwardingFunction3` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction3` |
| 1170 | `NdrProxyForwardingFunction30` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction30` |
| 1171 | `NdrProxyForwardingFunction31` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction31` |
| 1172 | `NdrProxyForwardingFunction32` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction32` |
| 1173 | `NdrProxyForwardingFunction4` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction4` |
| 1174 | `NdrProxyForwardingFunction5` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction5` |
| 1175 | `NdrProxyForwardingFunction6` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction6` |
| 1176 | `NdrProxyForwardingFunction7` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction7` |
| 1177 | `NdrProxyForwardingFunction8` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction8` |
| 1178 | `NdrProxyForwardingFunction9` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.NdrProxyForwardingFunction9` |
| 1179 | `ObjectStublessClient10` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient10` |
| 1180 | `ObjectStublessClient11` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient11` |
| 1181 | `ObjectStublessClient12` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient12` |
| 1182 | `ObjectStublessClient13` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient13` |
| 1183 | `ObjectStublessClient14` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient14` |
| 1184 | `ObjectStublessClient15` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient15` |
| 1185 | `ObjectStublessClient16` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient16` |
| 1186 | `ObjectStublessClient17` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient17` |
| 1187 | `ObjectStublessClient18` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient18` |
| 1188 | `ObjectStublessClient19` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient19` |
| 1189 | `ObjectStublessClient20` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient20` |
| 1190 | `ObjectStublessClient21` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient21` |
| 1191 | `ObjectStublessClient22` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient22` |
| 1192 | `ObjectStublessClient23` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient23` |
| 1193 | `ObjectStublessClient24` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient24` |
| 1194 | `ObjectStublessClient25` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient25` |
| 1195 | `ObjectStublessClient26` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient26` |
| 1196 | `ObjectStublessClient27` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient27` |
| 1197 | `ObjectStublessClient28` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient28` |
| 1198 | `ObjectStublessClient29` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient29` |
| 1199 | `ObjectStublessClient3` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient3` |
| 1200 | `ObjectStublessClient30` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient30` |
| 1201 | `ObjectStublessClient31` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient31` |
| 1202 | `ObjectStublessClient32` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient32` |
| 1203 | `ObjectStublessClient4` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient4` |
| 1204 | `ObjectStublessClient5` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient5` |
| 1205 | `ObjectStublessClient6` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient6` |
| 1206 | `ObjectStublessClient7` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient7` |
| 1207 | `ObjectStublessClient8` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient8` |
| 1208 | `ObjectStublessClient9` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-midlproxystub-l1-1-0.ObjectStublessClient9` |
| 1278 | `ProgIDFromCLSID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.ProgIDFromCLSID` |
| 1283 | `PropVariantClear` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.PropVariantClear` |
| 1284 | `PropVariantCopy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.PropVariantCopy` |
| 1295 | `RoGetAgileReference` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-1.RoGetAgileReference` |
| 1314 | `SetErrorInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.CoSetErrorInfo` |
| 1335 | `StringFromCLSID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.StringFromCLSID` |
| 1336 | `StringFromGUID2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.StringFromGUID2` |
| 1337 | `StringFromIID` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-l1-1-0.StringFromIID` |
| 1338 | `UpdateDCOMSettings` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.UpdateDCOMSettings` |
| 1339 | `UpdateProcessTracing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-com-private-l1-1-1.UpdateProcessTracing` |
| 1344 | `WdtpInterfacePointer_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserFree` |
| 1345 | `WdtpInterfacePointer_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserFree64` |
| 1346 | `WdtpInterfacePointer_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserMarshal` |
| 1347 | `WdtpInterfacePointer_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserMarshal64` |
| 1348 | `WdtpInterfacePointer_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserSize` |
| 1349 | `WdtpInterfacePointer_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserSize64` |
| 1350 | `WdtpInterfacePointer_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserUnmarshal` |
| 1351 | `WdtpInterfacePointer_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.WdtpInterfacePointer_UserUnmarshal64` |
| 1239 | `OleDuplicateData` | `0x52D0` | 363 | UnwindData |  |
| 809 | `ClipboardProcessUninitialize` | `0x8B50` | 91 | UnwindData |  |
| 995 | `CreateFileMoniker` | `0x90E0` | 886 | UnwindData |  |
| 1276 | `OleUninitialize` | `0xA2F0` | 208 | UnwindData |  |
| 998 | `CreateItemMoniker` | `0xB210` | 64 | UnwindData |  |
| 915 | `CoGetObject` | `0xB260` | 251 | UnwindData |  |
| 1145 | `MkParseDisplayName` | `0xBBA0` | 1,044 | UnwindData |  |
| 1142 | `IsValidInterface` | `0xCA40` | 64 | UnwindData |  |
| 1292 | `ReleaseStgMedium` | `0xD570` | 420 | UnwindData |  |
| 996 | `CreateGenericComposite` | `0xD810` | 820 | UnwindData |  |
| 1291 | `RegisterDragDrop` | `0xDD70` | 197 | UnwindData |  |
| 1242 | `OleGetClipboard` | `0xE450` | 698 | UnwindData |  |
| 1294 | `RevokeDragDrop` | `0xE9C0` | 187 | UnwindData |  |
| 863 | `CleanROTForApartment` | `0xEEA0` | 36 | UnwindData |  |
| 1012 | `DoDragDrop` | `0xF2C0` | 464 | UnwindData |  |
| 1264 | `OleRegGetUserType` | `0x13150` | 1,112 | UnwindData |  |
| 909 | `CoGetInterceptorForOle32` | `0x16330` | 1,022 | UnwindData |  |
| 990 | `CreateBindCtx` | `0x1ABC0` | 121 | UnwindData |  |
| 862 | `CheckInitDde` | `0x1BA20` | 213 | UnwindData |  |
| 1259 | `OleQueryCreateFromData` | `0x1C840` | 79 | UnwindData |  |
| 1260 | `OleQueryLinkFromData` | `0x1CA80` | 59 | UnwindData |  |
| 1139 | `IsEqualGUID` | `0x1E8E0` | 2,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `DllGetClassObject` | `0x1F410` | 84 | UnwindData |  |
| 1010 | `DllGetClassObjectWOW` | `0x1F410` | 84 | UnwindData |  |
| 1027 | `GetRunningObjectTable` | `0x23EB0` | 130 | UnwindData |  |
| 1271 | `OleSetClipboard` | `0x266D0` | 1,127 | UnwindData |  |
| 1240 | `OleFlushClipboard` | `0x26B40` | 284 | UnwindData |  |
| 1253 | `OleLoadPictureExt` | `0x2AA20` | 277 | UnwindData |  |
| 1233 | `OleCreatePictureIndirectExt` | `0x2AB40` | 368 | UnwindData |  |
| 1266 | `OleRun` | `0x2E450` | 120 | UnwindData |  |
| 1354 | `WriteFmtUserTypeStg` | `0x2E4D0` | 1,229 | UnwindData |  |
| 1356 | `WriteStringStream` | `0x2EC60` | 192 | UnwindData |  |
| 927 | `CoInitialize` | `0x30010` | 7,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `OleTranslateColorExt` | `0x31DA0` | 315 | UnwindData |  |
| 1238 | `OleDraw` | `0x32540` | 203 | UnwindData |  |
| 1265 | `OleReleaseEnumVerbCache` | `0x328C0` | 40 | UnwindData |  |
| 1002 | `CreateStdProgressIndicator` | `0x32D10` | 184 | UnwindData |  |
| 1293 | `RevokeActiveObjectExt` | `0x32F20` | 171 | UnwindData |  |
| 832 | `SetOleautModule` | `0x338D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `CreateClassMoniker` | `0x33A50` | 156 | UnwindData |  |
| 866 | `CoAllowSetForegroundWindow` | `0x349F0` | 132 | UnwindData |  |
| 1290 | `RegisterActiveObjectExt` | `0x34A80` | 246 | UnwindData |  |
| 1000 | `CreateOleAdviseHolder` | `0x36350` | 122 | UnwindData |  |
| 1272 | `OleSetContainedObject` | `0x372E0` | 132 | UnwindData |  |
| 1269 | `OleSaveToStream` | `0x373A0` | 178 | UnwindData |  |
| 992 | `CreateDataAdviseHolder` | `0x37760` | 127 | UnwindData |  |
| 803 | *Ordinal Only* | `0x37850` | 24 | UnwindData |  |
| 800 | *Ordinal Only* | `0x37CD0` | 44 | UnwindData |  |
| 1247 | `OleInitialize` | `0x381A0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `StgOpenStorageEx` | `0x383C0` | 67 | UnwindData |  |
| 1329 | `StgOpenStorage` | `0x38960` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `BindMoniker` | `0x38B10` | 156 | UnwindData |  |
| 1209 | `Ole32DllGetClassObject` | `0x39D20` | 2,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `StgCreateStorageEx` | `0x3A740` | 67 | UnwindData |  |
| 1007 | `DestroyRunningObjectTable` | `0x3ACC0` | 114 | UnwindData |  |
| 945 | `CoQueryReleaseObject` | `0x3B0B0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `ComPs_NdrDllCanUnloadNow` | `0x3B0B0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `IsValidIid` | `0x3B0B0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `IsValidPtrIn` | `0x3B0B0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `IsValidPtrOut` | `0x3B0B0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `StgOpenStorageOnILockBytes` | `0x3B320` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `ReadClassStm` | `0x3BA00` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `OleLockRunning` | `0x3BCD0` | 145 | UnwindData |  |
| 910 | `CoGetInterceptorFromTypeInfo` | `0x3BFA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `CreatePointerMoniker` | `0x3BFF0` | 127 | UnwindData |  |
| 1249 | `OleIsCurrentClipboard` | `0x3C450` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `WriteClassStm` | `0x3C4F0` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `OleIsRunning` | `0x3D1C0` | 116 | UnwindData |  |
| 1263 | `OleRegGetMiscStatus` | `0x3D5A0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `ReadClassStg` | `0x3DB80` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `ReadStorageProperties` | `0x3DB80` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `CoGetInterceptor` | `0x3DCF0` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `OleLoadFromStream` | `0x3E3C0` | 446 | UnwindData |  |
| 833 | `StdTypesGetClassObject` | `0x41C30` | 4,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | *Ordinal Only* | `0x42DC0` | 29 | UnwindData |  |
| 888 | `CoFreeAllLibraries` | `0x42FA0` | 5,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `SetWOWThunkGlobalPtr` | `0x42FA0` | 5,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `WriteClassStg` | `0x444C0` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `CoSetState` | `0x45850` | 8,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `DllRegisterServer` | `0x45850` | 8,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `CoInitializeWOW` | `0x47A70` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `CoRegisterMessageFilter` | `0x47B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `CoRegisterSurrogateEx` | `0x47B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `CoUnloadingWOW` | `0x47B50` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `HENHMETAFILE_UserFree` | `0x48750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `HENHMETAFILE_UserFree64` | `0x48760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `HENHMETAFILE_UserMarshal` | `0x48770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `HENHMETAFILE_UserMarshal64` | `0x48780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `HENHMETAFILE_UserSize` | `0x48790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `HENHMETAFILE_UserSize64` | `0x487A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `HENHMETAFILE_UserUnmarshal` | `0x487B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `HENHMETAFILE_UserUnmarshal64` | `0x487C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `HMETAFILEPICT_UserFree` | `0x487D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `HMETAFILEPICT_UserFree64` | `0x487E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `HMETAFILEPICT_UserMarshal` | `0x487F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `HMETAFILEPICT_UserMarshal64` | `0x48800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `HMETAFILEPICT_UserSize` | `0x48810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `HMETAFILEPICT_UserSize64` | `0x48820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `HMETAFILEPICT_UserUnmarshal` | `0x48830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `HMETAFILEPICT_UserUnmarshal64` | `0x48840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `HMETAFILE_UserFree` | `0x48850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `HMETAFILE_UserFree64` | `0x48860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `HMETAFILE_UserMarshal` | `0x48870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `HMETAFILE_UserMarshal64` | `0x48880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `HMETAFILE_UserSize` | `0x48890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `HMETAFILE_UserSize64` | `0x488A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `HMETAFILE_UserUnmarshal` | `0x488B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `HMETAFILE_UserUnmarshal64` | `0x488C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `SNB_UserFree` | `0x488D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `SNB_UserFree64` | `0x488E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `SNB_UserMarshal` | `0x488F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `SNB_UserMarshal64` | `0x48900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `SNB_UserSize` | `0x48910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `SNB_UserSize64` | `0x48920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `SNB_UserUnmarshal` | `0x48930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `SNB_UserUnmarshal64` | `0x48940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `STGMEDIUM_UserFree` | `0x48950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `STGMEDIUM_UserFree64` | `0x48960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `STGMEDIUM_UserMarshal` | `0x48970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `STGMEDIUM_UserMarshal64` | `0x48980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `STGMEDIUM_UserSize` | `0x48990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `STGMEDIUM_UserSize64` | `0x489A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `STGMEDIUM_UserUnmarshal` | `0x489B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `STGMEDIUM_UserUnmarshal64` | `0x489C0` | 10,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `CoAicGetTokenForCOM` | `0x4B180` | 111 | UnwindData |  |
| 870 | `CoCheckElevationEnabled` | `0x4B200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `CoGetSystemWow64DirectoryW` | `0x4B220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `DeletePatternAndExtensionTables` | `0x4B240` | 86 | UnwindData |  |
| 997 | `CreateILockBytesOnHGlobal` | `0x4B7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `FmtIdToPropStgName` | `0x4B7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `GetConvertStg` | `0x4B7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `GetDocumentBitStg` | `0x4B800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `GetHGlobalFromILockBytes` | `0x4B820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `PropStgNameToFmtId` | `0x4B840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `PropSysAllocString` | `0x4B860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `PropSysFreeString` | `0x4B880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `PropVariantChangeType` | `0x4B8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `StgConvertPropertyToVariant` | `0x4B8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `StgConvertVariantToProperty` | `0x4B8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `StgCreateDocfileOnILockBytes` | `0x4B900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `StgCreateDocfile` | `0x4B920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `StgCreatePropSetStg` | `0x4B940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `StgCreatePropStg` | `0x4B960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `StgGetIFillLockBytesOnFile` | `0x4B980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `StgGetIFillLockBytesOnILockBytes` | `0x4B9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `StgIsStorageFile` | `0x4B9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `StgIsStorageILockBytes` | `0x4B9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `StgOpenAsyncDocfileOnIFillLockBytes` | `0x4BA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `StgOpenPropStg` | `0x4BA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `StgOpenStorageOnHandle` | `0x4BA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `StgPropertyLengthAsVariant` | `0x4BA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `StgSetTimes` | `0x4BA80` | 9,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `CreateAntiMoniker` | `0x4E100` | 106 | UnwindData |  |
| 999 | `CreateObjrefMoniker` | `0x4E170` | 109 | UnwindData |  |
| 1146 | `MonikerCommonPrefixWith` | `0x51730` | 148 | UnwindData |  |
| 1147 | `MonikerRelativePathTo` | `0x517D0` | 475 | UnwindData |  |
| 1015 | `FindExt` | `0x542B0` | 140 | UnwindData |  |
| 1019 | `GetClassFile` | `0x54350` | 19,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `CoBuildVersion` | `0x59090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `OleBuildVersion` | `0x59090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `CoDosDateTimeToFileTime` | `0x590A0` | 63 | UnwindData |  |
| 887 | `CoFileTimeToDosDateTime` | `0x590F0` | 76 | UnwindData |  |
| 889 | `CoFreeLibrary` | `0x59150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `CoInstall` | `0x59160` | 255 | UnwindData |  |
| 935 | `CoLoadLibrary` | `0x59270` | 34 | UnwindData |  |
| 1140 | `IsRoInitializeASTAAllowedInDesktop` | `0x592A0` | 91 | UnwindData |  |
| 975 | `CoTryGetInterceptorForAppModelVirtualization` | `0x5BFC0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `ComPs_NdrDllGetClassObject` | `0x5C1E0` | 267 | UnwindData |  |
| 987 | `ComPs_NdrDllRegisterProxy` | `0x5C8C0` | 44 | UnwindData |  |
| 988 | `ComPs_NdrDllUnregisterProxy` | `0x5C900` | 41 | UnwindData |  |
| 1026 | `GetObjectFromRotByPath` | `0x6A2A0` | 93 | UnwindData |  |
| 1005 | `DdeBindToObject` | `0x6AB50` | 799 | UnwindData |  |
| 1217 | `OleCreate` | `0x7BCA0` | 127 | UnwindData |  |
| 1220 | `OleCreateEx` | `0x7BD30` | 564 | UnwindData |  |
| 1222 | `OleCreateFromData` | `0x7BF70` | 127 | UnwindData |  |
| 1223 | `OleCreateFromDataEx` | `0x7C000` | 616 | UnwindData |  |
| 1224 | `OleCreateFromFile` | `0x7C270` | 141 | UnwindData |  |
| 1225 | `OleCreateFromFileEx` | `0x7C310` | 645 | UnwindData |  |
| 1226 | `OleCreateLink` | `0x7C5A0` | 127 | UnwindData |  |
| 1227 | `OleCreateLinkEx` | `0x7C630` | 388 | UnwindData |  |
| 1228 | `OleCreateLinkFromData` | `0x7C7C0` | 127 | UnwindData |  |
| 1229 | `OleCreateLinkFromDataEx` | `0x7C850` | 761 | UnwindData |  |
| 1230 | `OleCreateLinkToFile` | `0x7CB50` | 127 | UnwindData |  |
| 1231 | `OleCreateLinkToFileEx` | `0x7CBE0` | 693 | UnwindData |  |
| 1235 | `OleCreateStaticFromData` | `0x7CEA0` | 847 | UnwindData |  |
| 1237 | `OleDoAutoConvert` | `0x7D200` | 343 | UnwindData |  |
| 1251 | `OleLoad` | `0x7D360` | 289 | UnwindData |  |
| 1258 | `OleNoteObjectVisible` | `0x7D960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `OleSave` | `0x7D980` | 180 | UnwindData |  |
| 1288 | `ReadOleStg` | `0x7DD00` | 376 | UnwindData |  |
| 1312 | `SetConvertStg` | `0x7DE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `SetDocumentBitStg` | `0x7DEA0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `WriteOleStg` | `0x7E2D0` | 118 | UnwindData |  |
| 1248 | `OleInitializeWOW` | `0x7E5D0` | 25 | UnwindData |  |
| 1287 | `ReadFmtUserTypeStg` | `0x7ECA0` | 232 | UnwindData |  |
| 993 | `CreateDataCache` | `0x82960` | 294 | UnwindData |  |
| 1243 | `OleGetClipboardWithEnterpriseInfo` | `0x87F50` | 1,169 | UnwindData |  |
| 804 | *Ordinal Only* | `0x8A530` | 44 | UnwindData |  |
| 802 | `OleGetPackageClipboardOwner` | `0x8A790` | 52 | UnwindData |  |
| 1013 | `DragDropSetFDT` | `0x94390` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | *Ordinal Only* | `0x94420` | 38 | UnwindData |  |
| 820 | *Ordinal Only* | `0x94450` | 294 | UnwindData |  |
| 821 | *Ordinal Only* | `0x94580` | 269 | UnwindData |  |
| 823 | *Ordinal Only* | `0x946A0` | 482 | UnwindData |  |
| 1138 | `IsAccelerator` | `0x95AB0` | 445 | UnwindData |  |
| 1232 | `OleCreateMenuDescriptor` | `0x95D70` | 377 | UnwindData |  |
| 1236 | `OleDestroyMenuDescriptor` | `0x95EF0` | 76 | UnwindData |  |
| 1273 | `OleSetMenuDescriptor` | `0x95F50` | 454 | UnwindData |  |
| 1274 | `OleTranslateAccelerator` | `0x96120` | 244 | UnwindData |  |
| 1218 | `OleCreateDefaultHandler` | `0x99B40` | 31 | UnwindData |  |
| 1219 | `OleCreateEmbeddingHelper` | `0x99B70` | 312 | UnwindData |  |
| 1241 | `OleGetAutoConvert` | `0x9A5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `OleSetAutoConvert` | `0x9A5F0` | 282 | UnwindData |  |
| 1244 | `OleGetIconOfClass` | `0x9BB30` | 353 | UnwindData |  |
| 1245 | `OleGetIconOfFile` | `0x9BCA0` | 847 | UnwindData |  |
| 1257 | `OleMetafilePictFromIconAndLabel` | `0x9C000` | 1,624 | UnwindData |  |
| 1261 | `OleRegEnumFormatEtc` | `0x9DAD0` | 115 | UnwindData |  |
| 1262 | `OleRegEnumVerbs` | `0x9E8D0` | 48,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `OleConvertIStorageToOLESTREAM` | `0xAA4C0` | 127 | UnwindData |  |
| 1212 | `OleConvertIStorageToOLESTREAMEx` | `0xAA550` | 509 | UnwindData |  |
| 1213 | `OleConvertOLESTREAMToIStorage` | `0xAA760` | 30 | UnwindData |  |
| 1214 | `OleConvertOLESTREAMToIStorage2` | `0xAA790` | 201 | UnwindData |  |
| 1215 | `OleConvertOLESTREAMToIStorageEx` | `0xAA860` | 68 | UnwindData |  |
| 1216 | `OleConvertOLESTREAMToIStorageEx2` | `0xAA8B0` | 529 | UnwindData |  |
| 1277 | `OpenOrCreateStream` | `0xAB7E0` | 114 | UnwindData |  |
| 1289 | `ReadStringStream` | `0xAB860` | 192 | UnwindData |  |
| 1340 | `UtConvertDvtd16toDvtd32` | `0xAC8C0` | 612 | UnwindData |  |
| 1341 | `UtConvertDvtd32toDvtd16` | `0xACB30` | 775 | UnwindData |  |
| 1342 | `UtGetDvtd16Info` | `0xACE40` | 353 | UnwindData |  |
| 1343 | `UtGetDvtd32Info` | `0xACFB0` | 314 | UnwindData |  |
| 834 | `StdTypesRegisterServer` | `0xB8A60` | 14,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `OleCreateFontIndirectExt` | `0xBC380` | 375 | UnwindData |  |
| 1246 | `OleIconToCursorExt` | `0xBF4D0` | 1,192 | UnwindData |  |
| 1255 | `OleLoadPicturePathExt` | `0xBF980` | 75 | UnwindData |  |
| 1234 | `OleCreatePropertyFrameIndirectExt` | `0xC17A0` | 109 | UnwindData |  |
| 1254 | `OleLoadPictureFileExt` | `0xC1EF0` | 314 | UnwindData |  |
| 1268 | `OleSavePictureFileExt` | `0xC2030` | 242 | UnwindData |  |
| 805 | `CLIPFORMAT_UserFreeExt` | `0xC5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `CLIPFORMAT_UserMarshalExt` | `0xC5C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `CLIPFORMAT_UserSizeExt` | `0xC5C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `CLIPFORMAT_UserUnmarshalExt` | `0xC5C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `HPALETTE_UserFreeExt` | `0xC5C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `HPALETTE_UserMarshalExt` | `0xC5C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `HPALETTE_UserSizeExt` | `0xC5CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `HPALETTE_UserUnmarshalExt` | `0xC5CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `HWND_UserFree64Ext` | `0xC5CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `HWND_UserFreeExt` | `0xC5D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `HWND_UserMarshal64Ext` | `0xC5D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `HWND_UserMarshalExt` | `0xC5D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `HWND_UserSize64Ext` | `0xC5D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `HWND_UserSizeExt` | `0xC5D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `HWND_UserUnmarshal64Ext` | `0xC5DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `HWND_UserUnmarshalExt` | `0xC5DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `MonikerLoadTypeLib` | `0xC5DF0` | 215 | UnwindData |  |
| 828 | `STGMEDIUM_UserFreeExt` | `0xC5ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `STGMEDIUM_UserMarshalExt` | `0xC5EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `STGMEDIUM_UserSizeExt` | `0xC5F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `STGMEDIUM_UserUnmarshalExt` | `0xC5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `WriteStorageProperties` | `0xC5F50` | 72 | UnwindData |  |
| 1018 | `GetActiveObjectExt` | `0xC5FA0` | 153 | UnwindData |  |
