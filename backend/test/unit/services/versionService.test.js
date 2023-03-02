import versionService from "../../../src/services/versionService";

describe("Version string should be correct", () => {
  it("should return a valid version string", async () => {
    const theVersion = versionService.version;
    expect(theVersion).toEqual({
      version: 0.1,
    });
  });
});
