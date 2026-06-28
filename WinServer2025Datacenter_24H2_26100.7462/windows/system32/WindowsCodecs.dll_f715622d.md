# Binary Specification: WindowsCodecs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WindowsCodecs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f715622dadaf941f31ad915c0c2ca735edec0a6126a13989c4f1b0d1c82f752f`
* **Total Exported Functions:** 117

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 115 | `WICMatchMetadataContent` | `0x1F510` | 318 | UnwindData |  |
| 116 | `WICSerializeMetadataContent` | `0x22280` | 863 | UnwindData |  |
| 111 | `WICGetMetadataContentSize` | `0x25590` | 714 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x44850` | 163 | UnwindData |  |
| 112 | `WICMapGuidToShortName` | `0x4C250` | 288 | UnwindData |  |
| 113 | `WICMapSchemaToName` | `0x4D9B0` | 426 | UnwindData |  |
| 110 | `WICCreateImagingFactory_Proxy` | `0x91FB0` | 259 | UnwindData |  |
| 37 | `IWICBitmapFrameEncode_Initialize_Proxy` | `0x9BC70` | 32 | UnwindData |  |
| 50 | `IWICBitmapSource_GetSize_Proxy` | `0x9BC70` | 32 | UnwindData |  |
| 62 | `IWICFastMetadataEncoder_Commit_Proxy` | `0x9BC70` | 32 | UnwindData |  |
| 87 | `IWICMetadataQueryReader_GetContainerFormat_Proxy` | `0x9BC70` | 32 | UnwindData |  |
| 100 | `IWICPalette_InitializePredefined_Proxy` | `0x9BC70` | 32 | UnwindData |  |
| 44 | `IWICBitmapLock_GetStride_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 48 | `IWICBitmapSource_GetPixelFormat_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 54 | `IWICColorContext_InitializeFromMemory_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 58 | `IWICComponentInfo_GetCLSID_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 63 | `IWICFastMetadataEncoder_GetMetadataQueryWriter_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 85 | `IWICMetadataBlockReader_GetCount_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 97 | `IWICPalette_InitializeCustom_Proxy` | `0x9BCA0` | 32 | UnwindData |  |
| 5 | `IEnumString_Reset_WIC_Proxy` | `0x9C130` | 32 | UnwindData |  |
| 43 | `IWICBitmapLock_GetDataPointer_STA_Proxy` | `0x9C130` | 32 | UnwindData |  |
| 49 | `IWICBitmapSource_GetResolution_Proxy` | `0x9C130` | 32 | UnwindData |  |
| 86 | `IWICMetadataBlockReader_GetReaderByIndex_Proxy` | `0x9C130` | 32 | UnwindData |  |
| 90 | `IWICMetadataQueryReader_GetMetadataByName_Proxy` | `0x9C130` | 32 | UnwindData |  |
| 106 | `WICConvertBitmapSource` | `0xA2400` | 261 | UnwindData |  |
| 47 | `IWICBitmapSource_CopyPixels_Proxy` | `0xA2510` | 45 | UnwindData |  |
| 15 | `IWICBitmapCodecInfo_GetMimeTypes_Proxy` | `0xA5650` | 35 | UnwindData |  |
| 32 | `IWICBitmapFrameDecode_GetColorContexts_Proxy` | `0xA8790` | 32 | UnwindData |  |
| 60 | `IWICComponentInfo_GetSpecVersion_Proxy` | `0xA8790` | 32 | UnwindData |  |
| 76 | `IWICImagingFactory_CreateDecoderFromStream_Proxy` | `0xA9530` | 54 | UnwindData |  |
| 70 | `IWICImagingFactory_CreateBitmapFromSource_Proxy` | `0xA9720` | 35 | UnwindData |  |
| 18 | `IWICBitmapDecoder_GetDecoderInfo_Proxy` | `0xAAD40` | 32 | UnwindData |  |
| 46 | `IWICBitmapSource_CopyPalette_Proxy` | `0xAAD40` | 32 | UnwindData |  |
| 88 | `IWICMetadataQueryReader_GetEnumerator_Proxy` | `0xAAD40` | 32 | UnwindData |  |
| 99 | `IWICPalette_InitializeFromPalette_Proxy` | `0xAAD40` | 32 | UnwindData |  |
| 51 | `IWICBitmap_Lock_Proxy` | `0xAB1C0` | 32 | UnwindData |  |
| 61 | `IWICComponentInfo_GetVersion_Proxy` | `0xAB1C0` | 32 | UnwindData |  |
| 84 | `IWICImagingFactory_CreateStream_Proxy` | `0xAB4C0` | 37 | UnwindData |  |
| 105 | `IWICStream_InitializeFromMemory_Proxy` | `0xAB960` | 35 | UnwindData |  |
| 19 | `IWICBitmapDecoder_GetFrameCount_Proxy` | `0xAB990` | 32 | UnwindData |  |
| 27 | `IWICBitmapEncoder_GetMetadataQueryWriter_Proxy` | `0xAB990` | 32 | UnwindData |  |
| 35 | `IWICBitmapFrameEncode_Commit_Proxy` | `0xAB990` | 32 | UnwindData |  |
| 96 | `IWICPalette_HasAlpha_Proxy` | `0xAB990` | 32 | UnwindData |  |
| 34 | `IWICBitmapFrameDecode_GetThumbnail_Proxy` | `0xAB9E0` | 32 | UnwindData |  |
| 53 | `IWICBitmap_SetResolution_Proxy` | `0xAB9E0` | 32 | UnwindData |  |
| 109 | `WICCreateColorContext_Proxy` | `0xACA90` | 32 | UnwindData |  |
| 11 | `IWICBitmapCodecInfo_GetContainerFormat_Proxy` | `0xACAF0` | 32 | UnwindData |  |
| 23 | `IWICBitmapDecoder_GetThumbnail_Proxy` | `0xACAF0` | 32 | UnwindData |  |
| 24 | `IWICBitmapEncoder_Commit_Proxy` | `0xACAF0` | 32 | UnwindData |  |
| 20 | `IWICBitmapDecoder_GetFrame_Proxy` | `0xACC30` | 32 | UnwindData |  |
| 36 | `IWICBitmapFrameEncode_GetMetadataQueryWriter_Proxy` | `0xACC30` | 32 | UnwindData |  |
| 101 | `IWICPixelFormatInfo_GetBitsPerPixel_Proxy` | `0xACC30` | 32 | UnwindData |  |
| 93 | `IWICPalette_GetColorCount_Proxy` | `0xB3B10` | 59 | UnwindData |  |
| 55 | `IWICComponentFactory_CreateMetadataWriterFromReader_Proxy` | `0xB40D0` | 35 | UnwindData |  |
| 94 | `IWICPalette_GetColors_Proxy` | `0xB4520` | 34 | UnwindData |  |
| 67 | `IWICImagingFactory_CreateBitmapFromHBITMAP_Proxy` | `0xB4C00` | 48 | UnwindData |  |
| 81 | `IWICImagingFactory_CreatePalette_Proxy` | `0xB4CE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `IWICImagingFactory_CreateBitmapFromMemory_Proxy` | `0xB4D10` | 86 | UnwindData |  |
| 25 | `IWICBitmapEncoder_CreateNewFrame_Proxy` | `0xB6B00` | 37 | UnwindData |  |
| 80 | `IWICImagingFactory_CreateFormatConverter_Proxy` | `0xB6B00` | 37 | UnwindData |  |
| 103 | `IWICPixelFormatInfo_GetChannelMask_Proxy` | `0xB6BA0` | 45 | UnwindData |  |
| 7 | `IWICBitmapClipper_Initialize_Proxy` | `0xB6E90` | 32 | UnwindData |  |
| 21 | `IWICBitmapDecoder_GetMetadataQueryReader_Proxy` | `0xB6E90` | 32 | UnwindData |  |
| 31 | `IWICBitmapFlipRotator_Initialize_Proxy` | `0xB6E90` | 32 | UnwindData |  |
| 33 | `IWICBitmapFrameDecode_GetMetadataQueryReader_Proxy` | `0xB6E90` | 32 | UnwindData |  |
| 91 | `IWICMetadataQueryWriter_RemoveMetadataByName_Proxy` | `0xB6E90` | 32 | UnwindData |  |
| 102 | `IWICPixelFormatInfo_GetChannelCount_Proxy` | `0xB8370` | 32 | UnwindData |  |
| 104 | `IWICStream_InitializeFromIStream_Proxy` | `0xB8370` | 32 | UnwindData |  |
| 65 | `IWICImagingFactory_CreateBitmapClipper_Proxy` | `0xB8400` | 37 | UnwindData |  |
| 39 | `IWICBitmapFrameEncode_SetResolution_Proxy` | `0xB9320` | 52 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xBF420` | 16,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WICSetEncoderFormat_Proxy` | `0xC3670` | 418,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllFreeCodecResources` | `0x129A90` | 21 | UnwindData |  |
| 4 | `IEnumString_Next_WIC_Proxy` | `0x129BD0` | 32 | UnwindData |  |
| 6 | `IPropertyBag2_Write_Proxy` | `0x129C00` | 32 | UnwindData |  |
| 89 | `IWICMetadataQueryReader_GetLocation_Proxy` | `0x129C00` | 32 | UnwindData |  |
| 8 | `IWICBitmapCodecInfo_DoesSupportAnimation_Proxy` | `0x129C30` | 35 | UnwindData |  |
| 9 | `IWICBitmapCodecInfo_DoesSupportLossless_Proxy` | `0x129C60` | 35 | UnwindData |  |
| 10 | `IWICBitmapCodecInfo_DoesSupportMultiframe_Proxy` | `0x129C90` | 35 | UnwindData |  |
| 12 | `IWICBitmapCodecInfo_GetDeviceManufacturer_Proxy` | `0x129CC0` | 32 | UnwindData |  |
| 13 | `IWICBitmapCodecInfo_GetDeviceModels_Proxy` | `0x129CF0` | 32 | UnwindData |  |
| 14 | `IWICBitmapCodecInfo_GetFileExtensions_Proxy` | `0x129D20` | 35 | UnwindData |  |
| 16 | `IWICBitmapDecoder_CopyPalette_Proxy` | `0x129D50` | 32 | UnwindData |  |
| 92 | `IWICMetadataQueryWriter_SetMetadataByName_Proxy` | `0x129D50` | 32 | UnwindData |  |
| 95 | `IWICPalette_GetType_Proxy` | `0x129D50` | 32 | UnwindData |  |
| 17 | `IWICBitmapDecoder_GetColorContexts_Proxy` | `0x129D80` | 32 | UnwindData |  |
| 59 | `IWICComponentInfo_GetFriendlyName_Proxy` | `0x129D80` | 32 | UnwindData |  |
| 22 | `IWICBitmapDecoder_GetPreview_Proxy` | `0x129DB0` | 32 | UnwindData |  |
| 52 | `IWICBitmap_SetPalette_Proxy` | `0x129DB0` | 32 | UnwindData |  |
| 26 | `IWICBitmapEncoder_GetEncoderInfo_Proxy` | `0x129DE0` | 37 | UnwindData |  |
| 28 | `IWICBitmapEncoder_Initialize_Proxy` | `0x129E10` | 37 | UnwindData |  |
| 29 | `IWICBitmapEncoder_SetPalette_Proxy` | `0x129E40` | 37 | UnwindData |  |
| 30 | `IWICBitmapEncoder_SetThumbnail_Proxy` | `0x129E70` | 37 | UnwindData |  |
| 38 | `IWICBitmapFrameEncode_SetColorContexts_Proxy` | `0x129EA0` | 37 | UnwindData |  |
| 40 | `IWICBitmapFrameEncode_SetSize_Proxy` | `0x129ED0` | 41 | UnwindData |  |
| 41 | `IWICBitmapFrameEncode_SetThumbnail_Proxy` | `0x129F00` | 37 | UnwindData |  |
| 42 | `IWICBitmapFrameEncode_WriteSource_Proxy` | `0x129F30` | 93 | UnwindData |  |
| 45 | `IWICBitmapScaler_Initialize_Proxy` | `0x129FA0` | 43 | UnwindData |  |
| 56 | `IWICComponentFactory_CreateQueryWriterFromBlockWriter_Proxy` | `0x129FE0` | 35 | UnwindData |  |
| 57 | `IWICComponentInfo_GetAuthor_Proxy` | `0x12A010` | 32 | UnwindData |  |
| 64 | `IWICFormatConverter_Initialize_Proxy` | `0x12A040` | 68 | UnwindData |  |
| 66 | `IWICImagingFactory_CreateBitmapFlipRotator_Proxy` | `0x12A090` | 37 | UnwindData |  |
| 68 | `IWICImagingFactory_CreateBitmapFromHICON_Proxy` | `0x12A0C0` | 35 | UnwindData |  |
| 71 | `IWICImagingFactory_CreateBitmapScaler_Proxy` | `0x12A0F0` | 37 | UnwindData |  |
| 72 | `IWICImagingFactory_CreateBitmap_Proxy` | `0x12A120` | 56 | UnwindData |  |
| 73 | `IWICImagingFactory_CreateComponentInfo_Proxy` | `0x12A160` | 37 | UnwindData |  |
| 74 | `IWICImagingFactory_CreateDecoderFromFileHandle_Proxy` | `0x12A190` | 53 | UnwindData |  |
| 75 | `IWICImagingFactory_CreateDecoderFromFilename_Proxy` | `0x12A1D0` | 63 | UnwindData |  |
| 77 | `IWICImagingFactory_CreateEncoder_Proxy` | `0x12A220` | 66 | UnwindData |  |
| 78 | `IWICImagingFactory_CreateFastMetadataEncoderFromDecoder_Proxy` | `0x12A270` | 35 | UnwindData |  |
| 79 | `IWICImagingFactory_CreateFastMetadataEncoderFromFrameDecode_Proxy` | `0x12A2A0` | 35 | UnwindData |  |
| 82 | `IWICImagingFactory_CreateQueryWriterFromReader_Proxy` | `0x12A2D0` | 35 | UnwindData |  |
| 83 | `IWICImagingFactory_CreateQueryWriter_Proxy` | `0x12A300` | 35 | UnwindData |  |
| 98 | `IWICPalette_InitializeFromBitmap_Proxy` | `0x12A330` | 32 | UnwindData |  |
| 107 | `WICCreateBitmapFromSection` | `0x12A360` | 52 | UnwindData |  |
| 108 | `WICCreateBitmapFromSectionEx` | `0x12A3A0` | 324 | UnwindData |  |
| 114 | `WICMapShortNameToGuid` | `0x12A4F0` | 172 | UnwindData |  |
