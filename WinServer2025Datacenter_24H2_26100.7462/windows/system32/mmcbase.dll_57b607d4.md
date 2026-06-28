# Binary Specification: mmcbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mmcbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `57b607d41368fa1c4937c4ac4d9b36a7d2a0535a1634a6ba2037417497d81684`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 101 | `?ReleaseSnapinInterface@BookKeeping@@SAJPEAUIUnknown@@H@Z` | `0x1230` | 289 | UnwindData |  |
| 26 | `?AddSnapinInterface@BookKeeping@@SA_NPEAUIUnknown@@PEBGAEAH@Z` | `0x13A0` | 448 | UnwindData |  |
| 102 | `?RemoveItem@BookKeeping@@SAJPEAX@Z` | `0x18B0` | 141 | UnwindData |  |
| 23 | `?AddItem@BookKeeping@@SAJAEAVItemHandle@@@Z` | `0x1B70` | 6 | UnwindData |  |
| 67 | `?InitInstance@BookKeeping@@SAJXZ` | `0x1F10` | 875 | UnwindData |  |
| 81 | `?LKResult2HRESULT@BookKeeping@@SAJ_J@Z` | `0x2290` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?FindItem@BookKeeping@@SAPEAVItemHandle@@PEAX@Z` | `0x3500` | 34 | UnwindData |  |
| 118 | `?ToHr@SC@mmcerror@@QEBAJXZ` | `0x3840` | 117 | UnwindData |  |
| 9 | `??1SC@mmcerror@@QEAA@XZ` | `0x38C0` | 81 | UnwindData |  |
| 110 | `?SetFunctionName@SC@mmcerror@@QEAAXPEBG@Z` | `0x3920` | 116 | UnwindData |  |
| 6 | `??0SC@mmcerror@@QEAA@J@Z` | `0x39A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??BSC@mmcerror@@QEBA_NXZ` | `0x39D0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?IsError@SC@mmcerror@@QEBA_NXZ` | `0x3CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?MakeSc@SC@mmcerror@@AEAAXW4facility_type@12@J@Z` | `0x3CF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?GetSnapinName@BookKeeping@@SAPEBGH@Z` | `0x3D90` | 142 | UnwindData |  |
| 122 | `?Trace_@SC@mmcerror@@QEBAXXZ` | `0x3EC0` | 75 | UnwindData |  |
| 14 | `??4SC@mmcerror@@QEAAAEAV01@AEBV01@@Z` | `0x3FA0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??4SC@mmcerror@@QEAAAEAV01@J@Z` | `0x43F0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?ScEmitOrPostpone@CEventBuffer@@QEAA?AVSC@mmcerror@@PEAUIDispatch@@JPEAVCComVariant@ATL@@H@Z` | `0x46D0` | 551 | UnwindData |  |
| 106 | `?ScFlushPostponed@CEventBuffer@@AEAA?AVSC@mmcerror@@XZ` | `0x4900` | 724 | UnwindData |  |
| 84 | `LoadStandardOverlays` | `0x4DF0` | 727 | UnwindData |  |
| 16 | `??7SC@mmcerror@@QEBAHXZ` | `0x50D0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0SC@mmcerror@@QEAA@AEBV01@@Z` | `0x53D0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?CheckCallingThreadID@SC@mmcerror@@QEAAXXZ` | `0x5960` | 56 | UnwindData |  |
| 1 | `??0?$CEventLock@UAppEvents@@@@QEAA@XZ` | `0x5DA0` | 27 | UnwindData |  |
| 51 | `GetEventBuffer` | `0x5DD0` | 110 | UnwindData |  |
| 17 | `??8SC@mmcerror@@QEBA_NAEBV01@@Z` | `0x5F40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `?FromWin32@SC@mmcerror@@QEAAAEAV12@J@Z` | `0x5F80` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?SetSnapinName@SC@mmcerror@@QEAAXPEBG@Z` | `0x6120` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?GetHinst@SC@mmcerror@@SAPEAUHINSTANCE__@@XZ` | `0x6190` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `GetStringModule` | `0x6190` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??8SC@mmcerror@@QEBA_NJ@Z` | `0x6270` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?TraceSnapinError@@YAXPEBGAEBVSC@mmcerror@@@Z` | `0x6A40` | 99 | UnwindData |  |
| 54 | `?GetHWnd@SC@mmcerror@@SAPEAUHWND__@@XZ` | `0x6AB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?GetNewSnapinInstanceId@BookKeeping@@SAHXZ` | `0x6B30` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?ScFromMMC@@YA?AVSC@mmcerror@@J@Z` | `0x72D0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?Clear@SC@mmcerror@@QEAAXXZ` | `0x75C0` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?TraceAndClear@SC@mmcerror@@QEAAXXZ` | `0x7BF0` | 31 | UnwindData |  |
| 45 | `?FromMMC@SC@mmcerror@@QEAAAEAV12@J@Z` | `0x7CA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?GetFacility@SC@mmcerror@@AEBA?AW4facility_type@12@XZ` | `0x7CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?GetCode@SC@mmcerror@@QEBAJXZ` | `0x7CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?GetMainThreadID@SC@mmcerror@@SAKXZ` | `0x7CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?IsLocked@CEventBuffer@@QEAA_NXZ` | `0x7D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?Lock@CEventBuffer@@QEAAXXZ` | `0x7D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??1CEventBuffer@@QEAA@XZ` | `0x7D20` | 5,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??9SC@mmcerror@@QEBA_NAEBV01@@Z` | `0x93A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??9SC@mmcerror@@QEBA_NJ@Z` | `0x93C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??_FSC@mmcerror@@QEAAXXZ` | `0x93E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?GetFunctionName@SC@mmcerror@@QEBAPEBGXZ` | `0x9440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?GetSnapinName@SC@mmcerror@@QEBAPEBGXZ` | `0x9450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?HrFromSc@@YAJAEBVSC@mmcerror@@@Z` | `0x9460` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `?SCODEFromSc@@YAJAEBVSC@mmcerror@@@Z` | `0x9460` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?AddSnapin@BookKeeping@@SAJPEBVCStr@@AEAH@Z` | `0xBCF0` | 121 | UnwindData |  |
| 30 | `?DumpWatsonTables@BookKeeping@@SAJPEAXPEBGH@Z` | `0xBD70` | 428 | UnwindData |  |
| 31 | `?EnableDiagnosticMessageBox@BookKeeping@@SA_N_N@Z` | `0xBF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?FindAllSnapinUIThreads@BookKeeping@@SAJHPEAPEAKPEAK@Z` | `0xBF50` | 172 | UnwindData |  |
| 35 | `?FindAllSnapinUIThreads@BookKeeping@@SAJPEAPEAKPEAK@Z` | `0xC010` | 160 | UnwindData |  |
| 37 | `?FindSnapin@BookKeeping@@SAAEBVSnapinBookkeepingInfo@@H@Z` | `0xC100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?FindSnapin@BookKeeping@@SAAEBVSnapinBookkeepingInfo@@PEAUIUnknown@@@Z` | `0xC110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?FindSnapin@BookKeeping@@SAAEBVSnapinBookkeepingInfo@@PEBVCStr@@@Z` | `0xC120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?FxSnapinException@BookKeeping@@SA_NHPEBG000HPEAUHWND__@@@Z` | `0xC130` | 212 | UnwindData |  |
| 62 | `?GetSnapinModuleName@BookKeeping@@SAPEBGH@Z` | `0xC2A0` | 110 | UnwindData |  |
| 68 | `?InterfaceFailure@BookKeeping@@SAXHPEBG0@Z` | `0xC320` | 48 | UnwindData |  |
| 69 | `?InterfaceMethodActivationContextException@BookKeeping@@SAXHPEBG0KPEAU_EXCEPTION_POINTERS@@@Z` | `0xC360` | 206 | UnwindData |  |
| 70 | `?InterfaceMethodException@BookKeeping@@SAXHPEBG0KPEAU_EXCEPTION_POINTERS@@@Z` | `0xC440` | 206 | UnwindData |  |
| 71 | `?InterfaceNotFound@BookKeeping@@SAXHPEBG@Z` | `0xC520` | 51 | UnwindData |  |
| 75 | `?InvalidInterface@BookKeeping@@SAXHPEBG0@Z` | `0xC560` | 48 | UnwindData |  |
| 76 | `?InvalidMMCInterface@BookKeeping@@SAXHPEBG0@Z` | `0xC5A0` | 48 | UnwindData |  |
| 77 | `?InvalidMMCInterfaceRelease@BookKeeping@@SAXHPEBG0@Z` | `0xC5E0` | 48 | UnwindData |  |
| 91 | `?MMCInterfaceError@BookKeeping@@SAXHPEBG0@Z` | `0xC620` | 50 | UnwindData |  |
| 92 | `?MMCInterfaceLeak@BookKeeping@@SAXHPEBG@Z` | `0xC660` | 53 | UnwindData |  |
| 93 | `?MMCInterfaceMethodException@BookKeeping@@SAXHPEBG0KPEAU_EXCEPTION_POINTERS@@W4_SnapinError@1@@Z` | `0xC6A0` | 201 | UnwindData |  |
| 94 | `?MMCNullInterface@BookKeeping@@SAXHPEBG0@Z` | `0xC770` | 50 | UnwindData |  |
| 98 | `?RegisterSnapinInterfaceErrorHandler@BookKeeping@@SAP6A_NAEAVSnapinBookkeepingInfo@@W4_SnapinError@1@PEBG222KPEAU_EXCEPTION_POINTERS@@@ZP6A_N012222K3@Z@Z` | `0xC7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?RegisterThread@BookKeeping@@SAJHHKW4SnapinThreadFlags@1@@Z` | `0xC7D0` | 182 | UnwindData |  |
| 124 | `?UnregisterAllSnapinInstanceThreads@BookKeeping@@SAJH@Z` | `0xCE50` | 131 | UnwindData |  |
| 125 | `?UnregisterThread@BookKeeping@@SAJHK@Z` | `0xCEE0` | 146 | UnwindData |  |
| 135 | `ReportFxSnapinException` | `0xD050` | 7,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?IsValid@ItemHandle@@SA_NPEBV1@@Z` | `0xEC30` | 74 | UnwindData |  |
| 32 | `?ExceptionFilter@CMMCWatsonAPI@@SAJPEAU_EXCEPTION_POINTERS@@H@Z` | `0x11270` | 431 | UnwindData |  |
| 40 | `?ForceException@CMMCWatsonAPI@@SAXH@Z` | `0x11430` | 38 | UnwindData |  |
| 4 | `??0CMMCStrongReferences@@AEAA@XZ` | `0x12290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??4CMMCStrongReferences@@QEAAAEAV0@$$QEAV0@@Z` | `0x122B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??4CMMCStrongReferences@@QEAAAEAV0@AEBV0@@Z` | `0x122D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?AddRef@CMMCStrongReferences@@SAKXZ` | `0x12370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetComObjectEventSource` | `0x12390` | 131 | UnwindData |  |
| 61 | `?GetSingletonObject@CMMCStrongReferences@@CAAEAV1@XZ` | `0x12420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?InternalAddRef@CMMCStrongReferences@@AEAAKXZ` | `0x12430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?InternalLastRefReleased@CMMCStrongReferences@@AEAA_NXZ` | `0x12440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?InternalRelease@CMMCStrongReferences@@AEAAKXZ` | `0x12450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?LastRefReleased@CMMCStrongReferences@@SA_NXZ` | `0x12470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?Release@CMMCStrongReferences@@SAKXZ` | `0x12480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?ScGetConsoleEventDispatcher@CConsoleEventDispatcherProvider@@SA?AVSC@mmcerror@@AEAPEAVCConsoleEventDispatcher@@@Z` | `0x124A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?ScSetConsoleEventDispatcher@CConsoleEventDispatcherProvider@@SA?AVSC@mmcerror@@PEAVCConsoleEventDispatcher@@@Z` | `0x124D0` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CEventBuffer@@QEAA@AEBV0@@Z` | `0x13410` | 42 | UnwindData |  |
| 3 | `??0CEventBuffer@@QEAA@XZ` | `0x13440` | 28 | UnwindData |  |
| 7 | `??1?$CEventLock@UAppEvents@@@@QEAA@XZ` | `0x13470` | 24 | UnwindData |  |
| 10 | `??4?$CEventLock@UAppEvents@@@@QEAAAEAV0@AEBV0@@Z` | `0x134C0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??4CEventBuffer@@QEAAAEAV0@AEBV0@@Z` | `0x13810` | 42 | UnwindData |  |
| 123 | `?Unlock@CEventBuffer@@QEAAXXZ` | `0x13900` | 42 | UnwindData |  |
| 33 | `?FatalError@SC@mmcerror@@QEBAXXZ` | `0x14640` | 59 | UnwindData |  |
| 41 | `?FormatErrorIds@@YAXIVSC@mmcerror@@IPEAG@Z` | `0x14690` | 162 | UnwindData |  |
| 42 | `?FormatErrorShort@@YAXVSC@mmcerror@@IPEAG@Z` | `0x14740` | 76 | UnwindData |  |
| 43 | `?FormatErrorString@@YAXPEBGVSC@mmcerror@@IPEAGH@Z` | `0x147A0` | 44 | UnwindData |  |
| 44 | `?FromLastError@SC@mmcerror@@QEAAAEAV12@XZ` | `0x147E0` | 65 | UnwindData |  |
| 50 | `?GetErrorMessage@SC@mmcerror@@QEBAXIPEAG@Z` | `0x14830` | 369 | UnwindData |  |
| 55 | `?GetHelpFile@SC@mmcerror@@SAPEBGXZ` | `0x149B0` | 59 | UnwindData |  |
| 56 | `?GetHelpID@SC@mmcerror@@QEAAKXZ` | `0x14A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?GetModalHWND@SC@mmcerror@@SAPEAUHWND__@@XZ` | `0x14A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `?MMCErrorBox@@YAHII@Z` | `0x14A20` | 181 | UnwindData |  |
| 87 | `?MMCErrorBox@@YAHIVSC@mmcerror@@I@Z` | `0x14AE0` | 233 | UnwindData |  |
| 88 | `?MMCErrorBox@@YAHPEBGI@Z` | `0x14BD0` | 242 | UnwindData |  |
| 89 | `?MMCErrorBox@@YAHPEBGVSC@mmcerror@@I@Z` | `0x14CD0` | 154 | UnwindData |  |
| 90 | `?MMCErrorBox@@YAHVSC@mmcerror@@I@Z` | `0x14D70` | 155 | UnwindData |  |
| 111 | `?SetHWnd@SC@mmcerror@@SAXPEAUHWND__@@@Z` | `0x14E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `?SetHinst@SC@mmcerror@@SAXPEAUHINSTANCE__@@@Z` | `0x14E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?SetMainThreadID@SC@mmcerror@@SAXK@Z` | `0x14E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?SetModalHWND@SC@mmcerror@@SAPEAUHWND__@@PEAU3@@Z` | `0x14E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?Throw@SC@mmcerror@@QEAAXJ@Z` | `0x14E70` | 19 | UnwindData |  |
| 117 | `?Throw@SC@mmcerror@@QEAAXXZ` | `0x14E90` | 111 | UnwindData |  |
| 120 | `?TraceError@@YAXPEBGAEBVSC@mmcerror@@@Z` | `0x14F10` | 62 | UnwindData |  |
| 95 | `MMCUpdateRegistry` | `0x15EE0` | 1,771 | UnwindData |  |
| 96 | `MMC_PickIconDlg` | `0x18050` | 153 | UnwindData |  |
| 132 | `EnterModalLoop` | `0x18CB0` | 189 | UnwindData |  |
| 133 | `InsideModalLoop` | `0x18D80` | 221 | UnwindData |  |
| 134 | `LeaveModalLoop` | `0x18E70` | 189 | UnwindData |  |
| 27 | `?Attach@DialogBoxDpiTracker@@QEAAPEAXXZ` | `0x1A220` | 143 | UnwindData |  |
| 83 | `?LoadDynamicLayoutResource@DialogBoxDpiTracker@@QEAAXPEAUHINSTANCE__@@PEAUHRSRC__@@@Z` | `0x1A300` | 69 | UnwindData |  |
| 103 | `?ResizeDynamicLayout@DialogBoxDpiTracker@@QEAAXXZ` | `0x1A350` | 45 | UnwindData |  |
| 127 | `?s_dwMainThreadID@SC@mmcerror@@0KA` | `0x2CC1C` | 1,820 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?s_pDispatcher@CConsoleEventDispatcherProvider@@0PEAVCConsoleEventDispatcher@@EA` | `0x2D338` | 13,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `?s_hInst@SC@mmcerror@@0PEAUHINSTANCE__@@EA` | `0x30690` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?s_hWnd@SC@mmcerror@@0PEAUHWND__@@EA` | `0x30698` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?s_CallDepth@SC@mmcerror@@0IA` | `0x306A0` | 536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?s_hWndModal@SC@mmcerror@@0PEAUHWND__@@EA` | `0x308B8` | 0 | Indeterminate |  |
