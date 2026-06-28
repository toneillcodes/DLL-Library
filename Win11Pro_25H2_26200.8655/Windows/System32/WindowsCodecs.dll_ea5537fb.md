# Binary Specification: WindowsCodecs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WindowsCodecs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea5537fb1100c1f3c6ae6a8804db499934093e566f51381bd37edf98c5947943`
* **Total Exported Functions:** 117

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 115 | `WICMatchMetadataContent` | `0x1F3E0` | 318 | UnwindData |  |
| 116 | `WICSerializeMetadataContent` | `0x22150` | 863 | UnwindData |  |
| 111 | `WICGetMetadataContentSize` | `0x25460` | 714 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x44660` | 163 | UnwindData |  |
| 112 | `WICMapGuidToShortName` | `0x4C060` | 288 | UnwindData |  |
| 113 | `WICMapSchemaToName` | `0x4D7C0` | 426 | UnwindData |  |
| 110 | `WICCreateImagingFactory_Proxy` | `0x911B0` | 259 | UnwindData |  |
| 37 | `IWICBitmapFrameEncode_Initialize_Proxy` | `0x9AF20` | 32 | UnwindData |  |
| 50 | `IWICBitmapSource_GetSize_Proxy` | `0x9AF20` | 32 | UnwindData |  |
| 62 | `IWICFastMetadataEncoder_Commit_Proxy` | `0x9AF20` | 32 | UnwindData |  |
| 87 | `IWICMetadataQueryReader_GetContainerFormat_Proxy` | `0x9AF20` | 32 | UnwindData |  |
| 100 | `IWICPalette_InitializePredefined_Proxy` | `0x9AF20` | 32 | UnwindData |  |
| 44 | `IWICBitmapLock_GetStride_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 48 | `IWICBitmapSource_GetPixelFormat_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 54 | `IWICColorContext_InitializeFromMemory_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 58 | `IWICComponentInfo_GetCLSID_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 63 | `IWICFastMetadataEncoder_GetMetadataQueryWriter_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 85 | `IWICMetadataBlockReader_GetCount_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 97 | `IWICPalette_InitializeCustom_Proxy` | `0x9AF50` | 32 | UnwindData |  |
| 5 | `IEnumString_Reset_WIC_Proxy` | `0x9B3E0` | 32 | UnwindData |  |
| 43 | `IWICBitmapLock_GetDataPointer_STA_Proxy` | `0x9B3E0` | 32 | UnwindData |  |
| 49 | `IWICBitmapSource_GetResolution_Proxy` | `0x9B3E0` | 32 | UnwindData |  |
| 86 | `IWICMetadataBlockReader_GetReaderByIndex_Proxy` | `0x9B3E0` | 32 | UnwindData |  |
| 90 | `IWICMetadataQueryReader_GetMetadataByName_Proxy` | `0x9B3E0` | 32 | UnwindData |  |
| 106 | `WICConvertBitmapSource` | `0xA1860` | 261 | UnwindData |  |
| 47 | `IWICBitmapSource_CopyPixels_Proxy` | `0xA1970` | 45 | UnwindData |  |
| 15 | `IWICBitmapCodecInfo_GetMimeTypes_Proxy` | `0xA4AB0` | 35 | UnwindData |  |
| 32 | `IWICBitmapFrameDecode_GetColorContexts_Proxy` | `0xA7D70` | 32 | UnwindData |  |
| 60 | `IWICComponentInfo_GetSpecVersion_Proxy` | `0xA7D70` | 32 | UnwindData |  |
| 76 | `IWICImagingFactory_CreateDecoderFromStream_Proxy` | `0xA8980` | 54 | UnwindData |  |
| 70 | `IWICImagingFactory_CreateBitmapFromSource_Proxy` | `0xA8B70` | 35 | UnwindData |  |
| 18 | `IWICBitmapDecoder_GetDecoderInfo_Proxy` | `0xAA180` | 32 | UnwindData |  |
| 46 | `IWICBitmapSource_CopyPalette_Proxy` | `0xAA180` | 32 | UnwindData |  |
| 88 | `IWICMetadataQueryReader_GetEnumerator_Proxy` | `0xAA180` | 32 | UnwindData |  |
| 99 | `IWICPalette_InitializeFromPalette_Proxy` | `0xAA180` | 32 | UnwindData |  |
| 51 | `IWICBitmap_Lock_Proxy` | `0xAA600` | 32 | UnwindData |  |
| 61 | `IWICComponentInfo_GetVersion_Proxy` | `0xAA600` | 32 | UnwindData |  |
| 84 | `IWICImagingFactory_CreateStream_Proxy` | `0xAA900` | 37 | UnwindData |  |
| 105 | `IWICStream_InitializeFromMemory_Proxy` | `0xAADA0` | 35 | UnwindData |  |
| 19 | `IWICBitmapDecoder_GetFrameCount_Proxy` | `0xAADD0` | 32 | UnwindData |  |
| 27 | `IWICBitmapEncoder_GetMetadataQueryWriter_Proxy` | `0xAADD0` | 32 | UnwindData |  |
| 35 | `IWICBitmapFrameEncode_Commit_Proxy` | `0xAADD0` | 32 | UnwindData |  |
| 96 | `IWICPalette_HasAlpha_Proxy` | `0xAADD0` | 32 | UnwindData |  |
| 34 | `IWICBitmapFrameDecode_GetThumbnail_Proxy` | `0xAAE20` | 32 | UnwindData |  |
| 53 | `IWICBitmap_SetResolution_Proxy` | `0xAAE20` | 32 | UnwindData |  |
| 109 | `WICCreateColorContext_Proxy` | `0xABED0` | 32 | UnwindData |  |
| 11 | `IWICBitmapCodecInfo_GetContainerFormat_Proxy` | `0xABF30` | 32 | UnwindData |  |
| 23 | `IWICBitmapDecoder_GetThumbnail_Proxy` | `0xABF30` | 32 | UnwindData |  |
| 24 | `IWICBitmapEncoder_Commit_Proxy` | `0xABF30` | 32 | UnwindData |  |
| 20 | `IWICBitmapDecoder_GetFrame_Proxy` | `0xAC070` | 32 | UnwindData |  |
| 36 | `IWICBitmapFrameEncode_GetMetadataQueryWriter_Proxy` | `0xAC070` | 32 | UnwindData |  |
| 101 | `IWICPixelFormatInfo_GetBitsPerPixel_Proxy` | `0xAC070` | 32 | UnwindData |  |
| 93 | `IWICPalette_GetColorCount_Proxy` | `0xB2EE0` | 59 | UnwindData |  |
| 55 | `IWICComponentFactory_CreateMetadataWriterFromReader_Proxy` | `0xB34A0` | 35 | UnwindData |  |
| 94 | `IWICPalette_GetColors_Proxy` | `0xB38F0` | 34 | UnwindData |  |
| 67 | `IWICImagingFactory_CreateBitmapFromHBITMAP_Proxy` | `0xB3FD0` | 48 | UnwindData |  |
| 81 | `IWICImagingFactory_CreatePalette_Proxy` | `0xB40B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `IWICImagingFactory_CreateBitmapFromMemory_Proxy` | `0xB40E0` | 86 | UnwindData |  |
| 25 | `IWICBitmapEncoder_CreateNewFrame_Proxy` | `0xB5ED0` | 37 | UnwindData |  |
| 80 | `IWICImagingFactory_CreateFormatConverter_Proxy` | `0xB5ED0` | 37 | UnwindData |  |
| 103 | `IWICPixelFormatInfo_GetChannelMask_Proxy` | `0xB5F70` | 45 | UnwindData |  |
| 7 | `IWICBitmapClipper_Initialize_Proxy` | `0xB6260` | 32 | UnwindData |  |
| 21 | `IWICBitmapDecoder_GetMetadataQueryReader_Proxy` | `0xB6260` | 32 | UnwindData |  |
| 31 | `IWICBitmapFlipRotator_Initialize_Proxy` | `0xB6260` | 32 | UnwindData |  |
| 33 | `IWICBitmapFrameDecode_GetMetadataQueryReader_Proxy` | `0xB6260` | 32 | UnwindData |  |
| 91 | `IWICMetadataQueryWriter_RemoveMetadataByName_Proxy` | `0xB6260` | 32 | UnwindData |  |
| 102 | `IWICPixelFormatInfo_GetChannelCount_Proxy` | `0xB7740` | 32 | UnwindData |  |
| 104 | `IWICStream_InitializeFromIStream_Proxy` | `0xB7740` | 32 | UnwindData |  |
| 65 | `IWICImagingFactory_CreateBitmapClipper_Proxy` | `0xB77D0` | 37 | UnwindData |  |
| 39 | `IWICBitmapFrameEncode_SetResolution_Proxy` | `0xB86F0` | 52 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xBED30` | 16,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WICSetEncoderFormat_Proxy` | `0xC2F80` | 418,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllFreeCodecResources` | `0x1293F0` | 21 | UnwindData |  |
| 4 | `IEnumString_Next_WIC_Proxy` | `0x129530` | 32 | UnwindData |  |
| 6 | `IPropertyBag2_Write_Proxy` | `0x129560` | 32 | UnwindData |  |
| 89 | `IWICMetadataQueryReader_GetLocation_Proxy` | `0x129560` | 32 | UnwindData |  |
| 8 | `IWICBitmapCodecInfo_DoesSupportAnimation_Proxy` | `0x129590` | 35 | UnwindData |  |
| 9 | `IWICBitmapCodecInfo_DoesSupportLossless_Proxy` | `0x1295C0` | 35 | UnwindData |  |
| 10 | `IWICBitmapCodecInfo_DoesSupportMultiframe_Proxy` | `0x1295F0` | 35 | UnwindData |  |
| 12 | `IWICBitmapCodecInfo_GetDeviceManufacturer_Proxy` | `0x129620` | 32 | UnwindData |  |
| 13 | `IWICBitmapCodecInfo_GetDeviceModels_Proxy` | `0x129650` | 32 | UnwindData |  |
| 14 | `IWICBitmapCodecInfo_GetFileExtensions_Proxy` | `0x129680` | 35 | UnwindData |  |
| 16 | `IWICBitmapDecoder_CopyPalette_Proxy` | `0x1296B0` | 32 | UnwindData |  |
| 92 | `IWICMetadataQueryWriter_SetMetadataByName_Proxy` | `0x1296B0` | 32 | UnwindData |  |
| 95 | `IWICPalette_GetType_Proxy` | `0x1296B0` | 32 | UnwindData |  |
| 17 | `IWICBitmapDecoder_GetColorContexts_Proxy` | `0x1296E0` | 32 | UnwindData |  |
| 59 | `IWICComponentInfo_GetFriendlyName_Proxy` | `0x1296E0` | 32 | UnwindData |  |
| 22 | `IWICBitmapDecoder_GetPreview_Proxy` | `0x129710` | 32 | UnwindData |  |
| 52 | `IWICBitmap_SetPalette_Proxy` | `0x129710` | 32 | UnwindData |  |
| 26 | `IWICBitmapEncoder_GetEncoderInfo_Proxy` | `0x129740` | 37 | UnwindData |  |
| 28 | `IWICBitmapEncoder_Initialize_Proxy` | `0x129770` | 37 | UnwindData |  |
| 29 | `IWICBitmapEncoder_SetPalette_Proxy` | `0x1297A0` | 37 | UnwindData |  |
| 30 | `IWICBitmapEncoder_SetThumbnail_Proxy` | `0x1297D0` | 37 | UnwindData |  |
| 38 | `IWICBitmapFrameEncode_SetColorContexts_Proxy` | `0x129800` | 37 | UnwindData |  |
| 40 | `IWICBitmapFrameEncode_SetSize_Proxy` | `0x129830` | 41 | UnwindData |  |
| 41 | `IWICBitmapFrameEncode_SetThumbnail_Proxy` | `0x129860` | 37 | UnwindData |  |
| 42 | `IWICBitmapFrameEncode_WriteSource_Proxy` | `0x129890` | 93 | UnwindData |  |
| 45 | `IWICBitmapScaler_Initialize_Proxy` | `0x129900` | 43 | UnwindData |  |
| 56 | `IWICComponentFactory_CreateQueryWriterFromBlockWriter_Proxy` | `0x129940` | 35 | UnwindData |  |
| 57 | `IWICComponentInfo_GetAuthor_Proxy` | `0x129970` | 32 | UnwindData |  |
| 64 | `IWICFormatConverter_Initialize_Proxy` | `0x1299A0` | 68 | UnwindData |  |
| 66 | `IWICImagingFactory_CreateBitmapFlipRotator_Proxy` | `0x1299F0` | 37 | UnwindData |  |
| 68 | `IWICImagingFactory_CreateBitmapFromHICON_Proxy` | `0x129A20` | 35 | UnwindData |  |
| 71 | `IWICImagingFactory_CreateBitmapScaler_Proxy` | `0x129A50` | 37 | UnwindData |  |
| 72 | `IWICImagingFactory_CreateBitmap_Proxy` | `0x129A80` | 56 | UnwindData |  |
| 73 | `IWICImagingFactory_CreateComponentInfo_Proxy` | `0x129AC0` | 37 | UnwindData |  |
| 74 | `IWICImagingFactory_CreateDecoderFromFileHandle_Proxy` | `0x129AF0` | 53 | UnwindData |  |
| 75 | `IWICImagingFactory_CreateDecoderFromFilename_Proxy` | `0x129B30` | 63 | UnwindData |  |
| 77 | `IWICImagingFactory_CreateEncoder_Proxy` | `0x129B80` | 66 | UnwindData |  |
| 78 | `IWICImagingFactory_CreateFastMetadataEncoderFromDecoder_Proxy` | `0x129BD0` | 35 | UnwindData |  |
| 79 | `IWICImagingFactory_CreateFastMetadataEncoderFromFrameDecode_Proxy` | `0x129C00` | 35 | UnwindData |  |
| 82 | `IWICImagingFactory_CreateQueryWriterFromReader_Proxy` | `0x129C30` | 35 | UnwindData |  |
| 83 | `IWICImagingFactory_CreateQueryWriter_Proxy` | `0x129C60` | 35 | UnwindData |  |
| 98 | `IWICPalette_InitializeFromBitmap_Proxy` | `0x129C90` | 32 | UnwindData |  |
| 107 | `WICCreateBitmapFromSection` | `0x129CC0` | 52 | UnwindData |  |
| 108 | `WICCreateBitmapFromSectionEx` | `0x129D00` | 324 | UnwindData |  |
| 114 | `WICMapShortNameToGuid` | `0x129E50` | 172 | UnwindData |  |
